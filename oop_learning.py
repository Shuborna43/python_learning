# OOP: Object oriented programming 
# OOP is a fundamental concept in python. It helps developers to build:
# 1. Modular application
# 2. Maintainable application 
# 3. Scalable applications 

# Detail:
# 1. Modular application: devided into small, reusable parts. 
# 2. Maintainable application: easy to update and fix. 
# 3. Scalable applications: can grow with more users or data 

# Key Features of OOP in python:
# Organizes code into classes and objects. 
# Encapsulation: Supports encapsulation to group data and methods together. 
# Inheritance: Enables inheritance for reusability and hierarchy. 
# Polymorphism: Allows polymorphism for flexible method implementation. 
# Improves Modularity, Scalability and Maitainability.  

# Characteristics of OOP:
# Class, Object, Encapsulation, Polymorphism, Inheritance, Abstruction 

# CLASS: collection of objects. classes are blueprints for creating objects. A class defines a set of attributes/ variables/properties/fields and methods that the created objects (instances). 
# 1. Classes are created by key word "class"  
# 2. attributes are the variables that belongs to a class 
# 3. Attributs are always public and can be accessed using "."

# Object: An object in a specific instance of a class. It holds its own set of data (instance variables) and can invoke methods defined by its class. Multiple objects can be created from the same class, each with its own unique atrributes. 


# Example: 
# define a class:
# class Dog:
#     sound_1 = "Bark"  #class attribute 
#     color_1 = "black"
#     sound_2 = "Ghew"
#     color_2 = "white"
#     sound_3 = "Mew"
#     color_3 = "brown"

# dog_1 = Dog() #object creation 
# dog_2 = Dog()
# dog_3 = Dog()

# print(dog_1.sound_1, dog_1.color_1, dog_2.sound_2, dog_2.color_2, dog_3.sound_3, dog_3.color_3) #accessing the class 


# string (str) method: 

# class Dog:
#     def __init__(self,name,age):          #the whole init function is a construtor
#         self.name = name 
#         self.age = age

#     def __str__(self):            #builtin method of parent class
#         return f"{self.name} is {self.age} years old"

# dog_1 = Dog("Tomy", 3)
# dog_2 = Dog("Lassy", 2)

# # print(dog_1)
# # print(dog_2)
# print(f"{dog_1}\n{dog_2}")


#self parameter: self parameter is a refrence to the current instance of the class. It allows us to acces atributes and methods of the object. 

# class Dog:
#     species = "Canine" #class level atribute 

#     def __init__(self,name,age): #the whole init function is a construtor
#         self.name = name #instance atribute/ variable
#         self.age = age #instance atribute/ variable
        

#     # def __str__(self):
#     #     return f"{self.name} is {self.age} years old"

# dog_1 = Dog("Tomy", 3) #dog_1, dog_2 are objects
# dog_2 = Dog("Lassy", 2) 

# print(dog_1.name, dog_1.age, dog_1.species)
# print(dog_2.name, dog_2.age, dog_2.species)


# __init__(): 
# 1. __init__() method is the constructor in python which automatically called when a new object is created. It initializes the attributes of the class.  

# Basic diffrence between class variables and instance variables:
# Class Variables: ther are shared across all instances of a class. it is defined at the class level outside any methods. All objcets of the class share the same value for a class variables unless, explicitly overridden in an object. 
# Instanc variables: variables that are unique to each instance(object) of a class. These are defined within the __init__() or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.  

# class Dog:
#     species = "Canine" #class level atribute 

#     def __init__(self,name,age): #the whole init function is a construtor
#         self.name = name #instance atribute/ variable
#         self.age = age #instance atribute/ variable
        

    # def __str__(self):
    #     return f"{self.name} is {self.age} years old"
#create objects:
# dog_1 = Dog("Tomy", 3) #create objects: dog_1, dog_2 are objects
# dog_2 = Dog("Lassy", 2) 

# #Access class and instance variables:
# print(dog_1.species) #class variable
# print(dog_1.name, dog_2.name) #instance variable 

# #modify instance variables:
# dog_1.name = "Max"
# print(dog_1.name)
# #modify class variables:
# Dog.species = "Feline"
# print(dog_1.species)
# print(dog_2.species)



#Inheritance:
# --------------
#Inheritance allows a class(child class) to acquire properties (attributes) and methods of another class (parent class). We use inheritance for:
# Code reusability
# Real world hierarchy
# Simplified maintenance 
# Method overriding  


# super():  
# parent class: Animal 

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def info(self): #method of parent class
#         print("animal name:", self.name) 

# # child class: Dog
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name) #calling the parent constructor 
#         self.breed = breed

#     def details(self): #method of child class
#         print(self.name, "is a", self.breed)

# #object creation
# d1 = Dog("Tomy", "Gloder retreaver")
# d1.info()
# d1.details()



#problem: parent class: vehicle, child class: car
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def info(self):
        print("Brand of the car is: ", self.brand, "and model is: ", self.model)



class Car(Vehicle):
    def __init__(self,brand,model,fuel):
        super().__init__(brand,model)
        self.fuel = fuel

    def details(self):
        print(self.model, "of", self.brand, "runs by", self.fuel)

c1 = Car("Toyota", "Allion", "Octane")
c1.info()
c1.details()





