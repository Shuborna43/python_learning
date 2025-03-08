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


# # task 3
# class TaxiLagbe:
#     def __init__(self,taxi_number, area):
#         self.taxi_number = taxi_number
#         self.area = area 
#         self.passenger_num=[]

#     def addPassenger (self, *name_fare):
#          self.name_fare = name_fare 
#          self.name,self.fare = self.name_fare.split ("_") # Splitting at '_'
#          self.fare = int (self.fare)
#          self.passenger_num.append(self.name)

#          print (f"Dear {self.name} Welcome to Taxilagbe.")

#     def printDetails (self):
       
#          print (f"Trip info for Taxi number: {self.taxi_number}\nThis taxi can only cover the the {self.area} area.\nTotal passenger: (len{self.passenger_num})\nPassenger lists:{self.name}\nTotal collected fare:{self.fare}") 


# # Write your code here

# class Sphere:
#      def __init__(self, ID,rad = 1, color = "white", pie=3.1416):
#           self.ID = ID
#           self.pie = pie
#           self.rad = rad 
#           self.color = color

#      def printDetails(self):
#           self.volume = (4/3)*self.pie*self.rad**3
#           print (f"Sphere ID:{self.ID}")
#           print (f"Color: {self.color}") 
#           print (f"Volume: {self.volume}")
          

         
#      def merge_sphere(self,*Sphere):
#           print(f"Spheres are being merged")
#           self.Sphere=Sphere
#         #   self.volume =0
#           self.volume += float(Sphere)
          


          

# sphere1 = Sphere("Sphere 1")
# print("1***************")
# sphere1.printDetails()
# print("2***************")
# sphere2 = Sphere("Sphere 2", 3)
# print("3***************")
# sphere2.printDetails()
# print("4***************")
# sphere3 = Sphere("Sphere 3", 2)
# print("5***************")
# sphere3.printDetails()
# print("6***************")
# sphere3.merge_sphere(sphere1,sphere2)
# print("7***************")
# sphere3.printDetails()
# print("8***************")
# sphere4 = Sphere("Sphere 4", 5, "Purple")
# print("9***************")
# sphere4.merge_sphere(sphere3)
# print("10***************")



class Sphere:
    def __init__(self, ID, rad=1, color="White", pie=3.1416):
        self.ID = ID
        self.rad = rad
        self.color = color
        self.pie = pie
        self.volume = (4/3) * self.pie * self.rad**3  # Calculate initial volume

    def printDetails(self):
        print(f"Sphere ID: {self.ID}")
        print(f"Color: {self.color}")
        print(f"Volume: {self.volume:.4f}")  # Format volume to 4 decimal places

    def merge_sphere(self, *spheres):
        print("Spheres are being merged")
        total_volume = self.volume  # Start with current sphere volume
        colors = {self.color}  # Store color of this sphere

        for sphere in spheres:
            total_volume += sphere.volume  # Add volumes
            colors.add(sphere.color)  # Collect colors

        # Update the radius based on total volume
        # new_radius = ((3 * total_volume) / (4 * self.pie)) ** (1/3)

        # Update sphere properties
        # self.rad = new_radius
        self.volume = total_volume

        # If different colors are present, set to 'Mixed Color'
        if len(colors) > 1:
            self.color = "Mixed Color"


# ✅ **Test Cases**
sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")

sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")

sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")

sphere3.merge_sphere(sphere1, sphere2)  # Merging sphere1 & sphere2 into sphere3
print("7***************")
sphere3.printDetails()
print("8***************")

sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)  # Merging sphere3 into sphere4
print("10***************")
sphere4.printDetails()





# Output:
# 1***************
# Sphere ID: Sphere 1
# Color: White
# Volume: 4.1888
# 2***************
# 3***************
# Sphere ID: Sphere 2
# Color: White
# Volume: 113.09759999999999
# 4***************
# 5***************
# Sphere ID: Sphere 3
# Color: White
# Volume: 33.5104
# 6***************
# Spheres are being merged
# 7***************
# Sphere ID: Sphere 3
# Color: White
# Volume: 150.7968
# 8***************

          