# 7. Problem: Student Management System using Encapsulation in Python

#  The program should clearly demonstrate Encapsulation by using private attributes and public methods to access and modify data.
# 1) Student Class
# Represents a single student.
# Class Requirements
# Private Attributes:
# student_id (int): unique ID of the student


# name (str): name of the student


# marks (int): marks obtained by the student


# Default value should be 0
# Constructor:
# __init__(student_id, name)


# Initializes student ID and name


# Sets marks to 0 initially
# Public Methods:
# get_student_id() → returns the student ID


# get_name() → returns the student name


# get_marks() → returns the student marks


# set_marks(marks) → updates the student marks
# 2) StudentManager Class
# Represents a collection of students.
# Class Requirements
# Private Attribute:
# students (list): stores multiple Student objects
# Constructor:
# __init__()


# Initializes an empty student list
# Methods:
# add_student(student)


# Adds a Student object to the list
# Prints: Student added: <name>

# update_marks(student_id, marks)
# Searches for a student using student ID
# If found, updates marks using setter method
# If not found, print: Student not found

# show_students()
#             Displays all students in the format:
#             <student_id> - <name> - <marks>
# Additional Requirement
# The program should take user input to:
# Add students


# Update student marks


# Display all students



# Expected Output (Example)
# Student added: Rahim
# Student added: Karim
# Marks updated for Rahim
# 101 - Rahim - 85
# 102 - Karim - 70

class Student:
    def __init__(self,student_id,name):
        self.__student_id = student_id 
        self.__name = name
        self.__marks = 0

    def get_student_id(self):
        return self.__student_id
    
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        self.__marks = marks

class StudentManager:
    def __init__(self):
        self.__students = []

    def add_student(self,student):
        self.__students.append(student)
        print(f"Student added: {student.get_name()}")

    def update_marks(self,student_id,marks):
        for stu in self.__students:
            if stu.get_student_id() == student_id:
                stu.set_marks(marks)  
                print("Marks updated")
            else:
                print("Student not found")
    
    def show_students(self):
        for stu in self.__students:
            print(f"{stu.get_student_id()}-{stu.get_name()}-{stu.get_marks()}")

manager = StudentManager()
while True:
    print("\n 1.Add students")
    print("2.Update student marks")
    print("3.Display all students")
    print("4.Exit program")

    choice = input("enter your choice:")
    if choice == "1":
        SID = int(input("enter student ID: "))
        Sname = input("enter student name: ")
    
        student = Student(SID,Sname)
        manager.add_student(student)


    elif choice == "2":
        Up_marks = int(input("enter student marks: ")) 
        SID = int(input("enter student ID: "))

        manager.update_marks(SID,Up_marks)

    elif choice == "3":
        manager.show_students()

    elif choice =="4":
        print("Exit")
        break 

    else:
        print("invalid choice")


    














    
        


