
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


# class Student:

#     def __init__(self, name, ID, department="CSE"):
#         self.name=name 
#         self.ID=ID
#         self.department=department
        

#     def dailyEffort (self,dailyEffort):
#         self.dailyEffort=dailyEffort

#     def printDetails (self):

#         print ("Name:", self.name)
#         print ("ID:", self.ID)
#         print ("Department:", self.department)
#         print ("Daily Effort:", self.dailyEffort, "hour(s)")


#         if self.dailyEffort<=2:
#             print ("Suggestion: Should give more effort!")
#         elif self.dailyEffort<=4:
#             print ("Suggestion: Keep up the good work!")
#         else:
#             print ("Suggestion: Excellent! Now motivate others.")


# Write your code here.

# harry = Student('Harry Potter', 123)
# harry.dailyEffort(3)
# harry.printDetails()  
# print('========================')
# john = Student("John Wick", 456, "BBA")
# john.dailyEffort(2)
# john.printDetails()
# print('========================')
# naruto = Student("Naruto Uzumaki", 777, "Ninja")
# naruto.dailyEffort(6)
# naruto.printDetails()


# Task:1
# Write the Farmer class with the required constructor,  methods to get the following output.

class Farmer:
    def __init__(self, name = None):
        self.name=name

    def addCrops (self,*Crops,Crops_number):
        self.Crops = Crops
        self.Crops_number =len(self.Crops)
    def addFishes (self,*Fishes, Fish_number):
        self.Fishes = Fishes 
        self.Fish_number = len(self.Fishes)
        if len(self.Fishes)==0:
            self.Fish_number="don't have any"
        else:
            self.Fish_number=len(self.Fishes)

    
    def showGoods (self):
        print (f"You have {self.Crops_number} crops: {self.Crops}. You {self.Fish_number} fish")
    
        

f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")


# # Welcome to your farm! 
# # ------------------- 
# # 3 crop(s) added. 
# # ------------------- 
# # No fish added. 
# # ------------------- 
# # 1 crop(s) added. 
# # ------------------- 
# # You have 4 crop(s): 
# # Rice,Jute,Cinnamon,Mustard 
# # You don't have any fish(s). 
# # ------------------- 
# # Welcome to your farm, Korim Mia!
#  ------------------- 
# 2 fish(s) added. 
# ------------------- 
# 2 crop(s) added. 
# ------------------- 
# 3 fish(s) added. 
# ------------------- 
# You have 2 crop(s): 
# Wheat,Potato 
# You have 5 fish(s): 
# Pangash,Magur,Koi,Tuna,Sardine 
# ------------------- 
# Welcome to your farm. Your farm ID is 2865127000! 
# ------------------- 
# No crop(s) added. 
# ------------------- 
# 1 fish(s) added. 
# ------------------- 
# You don't have any crop(s). 
# You have 1 fish(s): 
# Katla 
# -------------------




