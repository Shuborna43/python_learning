# Task 1
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



# task 2
# class Farmer:
#     def __init__(self, name_ID=None):
#         self.name_ID = name_ID

        
#         self.crop_num=[]
#         self.fish_num=[]

#         if self.name_ID==str: 
#           print(f"Welcome to your farm, {self.name_ID}!")

#         elif self.name_ID!=int:
#           print (f"Welcome to your farm. Your firm ID is {self.name_ID}!") 

#         else:
#           ("Welcome to your Farm!")
    
#     def addCrops (self,*Crops):
#         self.Crops = Crops
#         self.crop_num.extend(Crops)
      

#         if len(self.Crops)==0:
#           print ("No crop(s) added.")
#         else:
#           print(f"{len(self.Crops)} crop(s) added")

#     def addFishes (self,*Fishes):
#         self.Fishes = Fishes
#         self.fish_num.extend(Fishes)

#         if len(self.Fishes)==0:
#           print ("No fish(es) added.")
#         else:
#           print (f"{len(self.Fishes)} fish(es) added")

#     def showGoods (self):

#       if len(self.Fishes)==0:
#         print (f"You have {len(self.crop_num)}")
#         print ("crops:", ",".join(self.crop_num),".")
#         print ("You don't have any fish.")
#         #print (",".join(self.crop_num))

#       elif len(self.Crops)==0:
#         print (f"You don't have any crop(s).\nYou have {len(self.fish_num)}")
#         print ("fish(s):", ",".join(self.fish_num),".")

#       else:
#         print (f"You have {len(self.crop_num)}")
#         print ("crops:", ",".join(self.crop_num))
#         print (f"You have {len(self.fish_num)}")
#         print ("fish(s):", ",".join(self.fish_num),".")
    
        

# f1 = Farmer()
# print("-------------------")
# f1.addCrops('Rice', "Jute", "Cinnamon")
# print("-------------------")
# f1.addFishes()
# print("-------------------")
# f1.addCrops('Mustard')
# print("-------------------")
# f1.showGoods()
# print("-------------------")
# f2 = Farmer("Korim Mia")
# print("-------------------")
# f2.addFishes('Pangash', 'Magur')
# print("-------------------")
# f2.addCrops("Wheat", "Potato")
# print("-------------------")
# f2.addFishes("Koi", "Tuna", "Sardine")
# print("-------------------")
# f2.showGoods()
# print("-------------------")
# f3 = Farmer(2865127000)
# print("-------------------")
# f3.addCrops()
# print("-------------------")
# f3.addFishes("Katla")
# print("-------------------")
# f3.showGoods()
# print("-------------------")


# task 3
class TaxiLagbe:
    def __init__(self,taxi_number, area):
        self.taxi_number = taxi_number
        self.area = area 
        self.passenger_num=[]

    def addPassenger (self, *name_fare):
         self.name_fare = name_fare 
         self.name,self.fare = self.name_fare.split ("_") # Splitting at '_'
         self.fare = int (self.fare)
         self.passenger_num.append(self.name)

         print (f"Dear {self.name} Welcome to Taxilagbe.")

    def printDetails (self):
       
         print (f"Trip info for Taxi number: {self.taxi_number}\nThis taxi can only cover the the {self.area} area.\nTotal passenger: (len{self.passenger_num})\nPassenger lists:{self.name}\nTotal collected fare:{self.fare}") 


# Write your code here

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()
