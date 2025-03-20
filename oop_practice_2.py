#task#1
# class Student():
#     def __init__(self,name,cgpa = 0,credit = 9,department = "CSE",scholarship = " "):
#         self.name = name
#         self.cgpa = float(cgpa)
#         self.credit = int(credit)
#         self.department = department 
#         self.scholarship = scholarship
    
#     def checkScholarshipEligibility(self):
       
#         if self.credit >10:
#             if (self.cgpa >= 3.5 and self.cgpa <3.7): 
#                 self.scholarship = "Need-based scholarship" 
#                 print(f"{self.name} is eligible for {self.scholarship}")
#             elif (self.cgpa >= 3.7): 
#                 self.scholarship = "Merit-based scholarship"
#                 print(f"{self.name} is eligible for {self.scholarship}")
#             else:
#                 self.scholarship = "not eligible for scholarship"
#                 print(f"{self.name} is {self.scholarship}")

#         else:
#             self.scholarship = "No scholarship"
#             print(f"{self.name} is not eligible for scholarship")

#     def showDetails(self):
#         print (f"Name: {self.name}")
#         print (f"Department: {self.department}")
#         print (f"CGPA: {self.cgpa}")
#         print (f"Number of Credits: {self.credit}")
#         print (f"Scholarship Status: {self.scholarship}")

# print('--------------------------')
# std1 = Student("Alif", 3.99, 12)
# print('--------------------------')
# std1.checkScholarshipEligibility()
# print('--------------------------')
# std1.showDetails()
# print('--------------------------')
# std2 = Student("Mim", 3.4)
# std3 = Student("Henry", 3.5, 15,"BBA")
# print('--------------------------')
# std2.checkScholarshipEligibility()
# print('--------------------------')
# std3.checkScholarshipEligibility()
# print('--------------------------')
# std2.showDetails()
# print('--------------------------')
# std3.showDetails()
# print('--------------------------')
# std4 = Student("Bob", 4.0, 6, "CSE")
# print('--------------------------')
# std4.checkScholarshipEligibility()
# print('--------------------------')
# std4.showDetails()

# #task#2

class Foodie():
    def __init__(self,name):
        self.name = name
        self.item_num=[]

    def show_orders(self,*Items):
        self.Items = Items
        self.item_num.extend(Items)
        if len(self.item_num) == 0:
            print (f"{self.name} has {len(self.item_num)} items in the cart")
            print (f"Items:[]")
            print (f"Total spent: 0")

    def order(self,*item-unit):
        self.item-unit = item-unit



        
        


menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}

f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())




        