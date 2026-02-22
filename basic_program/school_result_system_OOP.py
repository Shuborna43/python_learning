from abc import ABC, abstractmethod
class StudentResult(ABC):
    def __init__(self,student_id,name,marks,attendance,has_co_curricular):
        self.__student_id = student_id
        self.__name = name 
        self.__marks = marks
        self.__attendance = attendance
        self.__has_co_curricular = has_co_curricular 

    def get_student_id(self):
        return self.__student_id 
    
    def get_name(self):
        return self.__name 
    
    def get_marks(self):
        return self.__marks
    
    def get_attendance(self):
        return self.__attendance
    
    def get_has_co_curricular(self):
        return self.__has_co_curricular
    
    @abstractmethod
    def calculate_gpa(self):
        pass

    @abstractmethod
    def attendance_penalty(self,gpa):
        pass

    @abstractmethod 
    def bonus_points(self,gpa):
        pass 

    def final_gpa(self):
        gpa = self.calculate_gpa() 
        gpa = self.attendance_penalty(gpa)
        gpa = self.bonus_points(gpa) 

        if gpa > 5.0:
            gpa = 5.0
        elif gpa < 0.0:
            gpa = 0.0

        return round(gpa,2) 
    
class SchoolStudent(StudentResult):
    def calculate_gpa(self):
        total = 0 
        for mark in self.get_marks():
            if mark >= 80:
                total += 5.0
            elif mark >= 70:
                total += 4.0
            elif mark >= 60:
                total += 3.5
            elif mark >= 50:
                total += 3.0
            elif mark >= 40:
                total += 2.0
            else:
                total+= 0.0 
        
        return total/len(self.get_marks())

    def attendance_penalty(self,gpa): 
        attendance = self.get_attendance() 
        if attendance < 60:
            return gpa - 1.0
        elif attendance < 75: 
            return gpa - 0.5
        
        return gpa
    
    def bonus_points(self,gpa):
        if self.get_has_co_curricular():
            return gpa +0.2
        return gpa 
    
    def scholarship_status(self,final_gpa):
        if final_gpa >= 4.8 and self.get_attendance() >= 85:
            return "Full Scholarship"
        
        elif final_gpa >= 4.5:
            return "Half Scholarship"
        
        else:
            return "No Scholarship"
 
students_list = []
n = int(input("Enter number of students: "))

for stu in range(n):
    print(f"\n Enter details for student {stu + 1} ")

    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")

    total_subject = int(input("Enter total number of subjects: "))
    marks = []
    for sub in range(total_subject):
        mark = float(input(f"Enter mark for subject {sub + 1}: "))
        marks.append(mark)

    attendance = int(input("Enter the % of attendance: ")) 
    co_curricular_activity = input("provide yes/no for scholarship: ").lower()
    has_co_curricular = True if co_curricular_activity == "yes" else False 

    student = SchoolStudent(student_id,student_name,marks,attendance,has_co_curricular)

    students_list.append(student)

print("\n ==== Student Results ====")
for student in students_list:
    final_gpa = student.final_gpa()
    scholarship = student.scholarship_status(final_gpa)

    print(f"ID: {student.get_student_id()}, Name: {student.get_name()}, GPA: {final_gpa}, Scholarship: {scholarship} ")



        






       