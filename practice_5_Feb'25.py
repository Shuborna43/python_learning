
# problem #1  
# Design the Student class in such a way so that the following code provides the expected output. 
# Hint:
# ●	Write the constructor with an appropriate default value for arguments.
# ●	Write the dailyEffort() method with appropriate arguments.
# ●	Write the printDetails() method. You can follow the printing suggestions below:
# ⮚	If hour <= 2 print 'Suggestion: Should give more effort!'
# ⮚	Else if hour <= 4 print 'Suggestion: Keep up the good work!'
# ⮚	Else print 'Suggestion: Excellent! Now motivate others.'
# [You are not allowed to change the code below]


class Student:

    def __init__(self, name, ID, department="CSE"):
        self.name=name 
        self.ID=ID
        self.department=department
        

    def dailyEffort (self,dailyEffort):
        self.dailyEffort=dailyEffort

    def printDetails (self):

        print ("Name:", self.name)
        print ("ID:", self.ID)
        print ("Department:", self.department)
        print ("Daily Effort:", self.dailyEffort, "hour(s)")


        if self.dailyEffort<=2:
            print ("Suggestion: Should give more effort!")
        elif self.dailyEffort<=4:
            print ("Suggestion: Keep up the good work!")
        else:
            print ("Suggestion: Excellent! Now motivate others.")


# Write your code here.

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()  
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()


