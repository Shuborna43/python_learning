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

# CLASS: collection of objects. classes are blueprints for creating objects. A class defines a set of attributes/ variables/properties/fields and methods that create objects (instances). 
# 1. Classes are created by key word "class"  
# 2. Attributes are the variables that belongs to a class 
# 3. Attributs are always public and can be accessed using "."

# Object: An object is a specific instance of a class. It holds its own set of data (instance variables) and can invoke methods defined by its class. Multiple objects can be created from the same class, each with its own unique atrributes. 


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


# string (str) method: it is a  builtin method than allows us to define a custom string representation of an object.  

# class Dog:
#     def __init__(self,name,age):          #the whole "__init__()" is a construtor
#         self.name = name                  #initialization of variable
#         self.age = age                    #initialization of variable

#     def __str__(self):                    #builtin method
#         return f"{self.name} is {self.age} years old"

# dog_1 = Dog("Tomy", 3)    #created object (dog_1) and gave instance variables ("Tomy", 3). 
# dog_2 = Dog("Lassy", 2)

# # print(dog_1)
# # print(dog_2)
# print(f"{dog_1}\n{dog_2}")


#self parameter: self parameter is a refrence to the current instance of the class. It allows us to access atributes and methods of the object. 

# class Dog:
#     species = "Canine" #class level atribute 

#     def __init__(self,name,age): #the whole " __init__()" is a construtor
#         self.name = name     #instance atribute/ variable initialization 
#         self.age = age       #instance atribute/ variable initialization 
        

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# dog_1 = Dog("Tomy", 3) #dog_1, dog_2 are objects
# dog_2 = Dog("Lassy", 2) 

# print(dog_1, dog_1.species)
# print(dog_2, dog_2.species)


# __init__(): 
# 1. __init__() method is the constructor in python which automatically called when a new object is created. It initializes the attributes of the class.  

# Basic diffrence between class variables and instance variables:
# Class Variables: they are shared across all instances of a class. it is defined at the class level outside any methods. All objcets of the class share the same value for a class variables unless, explicitly overridden in an object. 
# Instanc variables: variables that are unique to each instance(object) of a class. These are defined within the __init__() or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.  

# class Dog:
#     species = "Canine" #class level atribute 

#     def __init__(self,name,age): #the whole "__init__()" is a construtor
#         self.name = name         #instance atribute/ instance variable initailization 
#         self.age = age           #instance atribute/ instance variable initialization
        

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
# #create objects:
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


# super(): this function is used to call the parent classe's methods. in particular it is commonly used in child classes __init__() to initialize inheritate attributes. This function can be used when there is one parent class and if the child class has its own constructor.   



# parent class: Animal 
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def info(self):         #method of parent class
#         print("animal name:", self.name) 

# # child class: Dog
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)      #calling the parent constructor 
#         self.breed = breed

#     def details(self):              #method of child class
#         print(self.name, "is a", self.breed)

# # #object creation
# d1 = Dog("Tomy", "Gloder retreaver")
# d1.info()
# d1.details()



#problem: parent class: vehicle, child class: car
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def info(self):
#         print("Brand of the car is: ", self.brand, "and model is: ", self.model)



# class Car(Vehicle):
#     def __init__(self,brand,model,fuel):
#         super().__init__(brand,model)
#         self.fuel = fuel

#     def details(self):
#         print(self.model, "of", self.brand, "runs by", self.fuel)

# c1 = Car("Toyota", "Allion", "Octane")
# c1.info()
# c1.details()


# Types of Python inheritance:
# Inheritance can be used in different ways depending on how many parent and child classes are invovled. They help model, real world relationships more effectively and allow flexibility in code reuse. 

# 1. Single inheritance: In single inheritance, a child class inherits from just one parent class. 

# class Person:                          #class creation
#     def __init__(self,name):           #create constructor 
#         self.name = name               #variable initialization 

# class Employee(Person):                #create child class: Employee inherits from Person class. 
#     def showrole(self):                #a new function
#         print(self.name, "is an employee")

# employee1 = Employee("Farzana")        #object creation 
# employee1.showrole()                   #calling function 

#2. Multiple inheritance: In multiple inheritance, a child class can inherit from more than one parent class. 

# class Person:                   #parent class_1
#     def __init__(self,name):    #constructor of parent class_1
#         self.name = name        #initialization

# class Job:                      #parent class_2
#     def __init__(self,salary):  #constructor of parent class_2
#         self.salary = salary    #initialization

# class Employee(Person,Job):     #child class
#     def __init__(self,name,salary):     #constructor for initializing the variables of 2 parent class
#         Person.__init__(self,name)      #initializion parent class variable   
#         Job.__init__(self,salary)       #initializion parent class variable  

#     def details(self):                  #create function under child class  
#         print(self.name, "earns", "BDT",self.salary, "per month")

# employee1 = Employee("Farzana", 20000)   #create object and instance variable 
# employee1.details()                      #calling function 

# #3. Multi level inheritance: in multi-level inheritance a class is derived from another derived class (like a chain). 

class Person:
    def __init__(self,name):
        self.name = name 

class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)  #call the Person's constructor 
        self.salary = salary 

    def showrole(self):
        print(self.name, "earns BDT",self.salary)

    def unit (self,unit):
        print(self.name, "manages", unit, "unit")

class Manager(Employee):
    def department(self,dept):
        print(self.name, "manages", dept, "department")
        

manager1 = Manager("Farzana", 20000)
manager1.showrole()
manager1.unit("payment")
manager1.department("HR")

    
# 4. Hierarchical inheritance: multiple child classes inherit from the same parent class.

# class Person:
#     def __init__(self,name):
#         self.name = name

# class Employee(Person):
#     def role(self):
#         print(self.name, "works as an employee")

# class Intern(Person):
#     def role(self):
#         print(self.name, "is an intern")

# employee1 = Employee("Farzana")
# employee1.role()
# intern1 = Intern("Wadi")
# intern1.role()

#5. Hybrid inheritance: in hybrid inheritance is a combination of more than one type of inheritance.

# class Person:
#     def __init__(self,name):
#         self.name = name

# class Employee(Person):
#     def role(self):
#         print(self.name, "works as an employee")

# class Project:
#     def __init__(self,project_name):
#         self.project_name = project_name 

# class Teamlead(Employee, Project):
#     def __init__(self, name, project_name):
#         Employee.__init__(self,name)
#         Project.__init__(self,project_name)

#     def details(self):
#         print (self.name, "leads project", self.project_name)

# lead_1 = Teamlead("Adyan", "XYZ")
# lead_1.role()
# lead_1.details()











