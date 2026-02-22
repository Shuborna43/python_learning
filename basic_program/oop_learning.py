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

# # #modify instance variables:
# dog_1.name = "Max"
# print(dog_1.name)
# # #modify class variables:
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

# # #3. Multi level inheritance: in multi-level inheritance a class is derived from another derived class (like a chain). 

# class Person:
#     def __init__(self,name):
#         self.name = name 

# class Employee(Person):
#     def __init__(self,name,salary):
#         super().__init__(name)  #call the Person's constructor 
#         self.salary = salary 

#     def showrole(self):
#         print(self.name, "earns BDT",self.salary)

#     def unit (self,unit):
#         print(self.name, "manages", unit, "unit")

# class Manager(Employee):
#     def department(self,dept):
#         print(self.name, "manages", dept, "department")
        

# manager1 = Manager("Farzana", 20000)
# manager1.showrole()
# manager1.unit("payment")
# manager1.department("HR")

    
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

# Polymorphism: Polymorphism means many forms. It refers to the ability of an entity (function/object) to perform different actions based on the context. Technically in python, polymorphism allows same method, function or operator to behave differently depending on object it is working with. This makes code more flexible and reusable. 
# Why do we need polymorphism:
# 1. ensure consistant interfaces across different classes. 
# 2. Allows object to response diffrently to the same method call. 
# 3. Enables writing flexible, reusable codes that works across types. 
# 4. Simplifies testing and future extention of code.
# Types of pilymorphism: compile-time polymorphism (method overloading) and run-time polymorphism (method overriding).
# compile-time polymorphism (method overloading): 

# compile-time polymorphism example:

# class Calculator:
#     def multiply(self, a=1, b=1, *args):  #*args = unlimited aguments. argument is a tupple and it accepts multiple value. 

#         result = a*b 
#         for num in args:
#             result *= num 
#         return result 

# calc = Calculator()
# print(calc.multiply())
# print(calc.multiply(4))
# print(calc.multiply(2,3))
# print(calc.multiply(2,3,4,5,6,7))
# print(1*2*3*4*5*6*7)

# run-time polymorphism (method overriding):
# Example: 

# class Animal:
#     def sound(self):
#         return "some generic sound"
    
# class Dog(Animal):
#     def sound(self):
#         return "bark"
    
# class Cat(Animal):
#     def sound(self):
#         return "meow"

#polymorphic behavior 
# animals = [Animal(),Dog(),Cat()]
# for animal in animals:
#     print(animal.sound())

# Built-in polymorphism/ polymorphism in built-in fundtion: Python built-in functions like; len() and max() are polymorphic they work with different data types and return results based on type of object passed. Example;
# print(max(3,6,7,8))
# print(len("Shourov"))

# Duck typing: Polymorphism lets functions accept different object types as long as they support needed behavior. Using duck typing python focuses on whether an object has right method not its type allowing flexible and reusable code. 

# class Pen:
#     def use(self):
#         return 8877655
# class Eraser: 
#     def use(self):
#         return "erasing"

# def perform_task(tool):
#     print (tool.use()) 

# perform_task(Pen())
# perform_task(Eraser())

# Operator Polymorphism/Operator overloading: In python same operator can perform different task depending on operand types. This is known as operator overloading. 

# print(3+8)
# print("orrange"+"apple")
# print([3,4,5,6]+["O","P","G"])  


# Encapsulation: Encapsulation means hiding internal detail of a class and only exposing what's necessary. It helps to protect imporatnt data from being changed directly and keeps the codes secure and organized. 




# class Employee():
#     def __init__(self,name,salary):
#         self.name = name 
#         self.__salary = salary #to keep a variable as private need to give __( 2 underscore) before it. it is called name mangling)

# employee = Employee("Farzana",20000)

# print(employee.name)
# print(employee._Employee__salary)

# Why do we need encapsulation?: 
# Protects data from unauthorized access and accidental modification. 
# control data updates using getter abd setter methods with validation. 
# enhances modularity by hiding internal implementation detail. 
# simplifies maintenance through centralized data handling logic. 
# reflects real world scenerios like restricting direct access to a bank account balance. 

# Example:

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner 
#         self.__balance = balance 

#     def deposite(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -=amount 
#         else:
#             print("insufficient balance")

#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount("Farzana", 20000)
# #print (account.__balance)
# print(account.get_balance())
# account.deposite(400)
# print(account.get_balance())
# account.withdraw(600)
# print(account.get_balance())
# account.withdraw(40000)

# Access specifiers: it defines how class members (variables and methods) can be accessed from outside the class. They help in implementing encapsulation by controlling the visibility of data. There are 3 types of access specifiers: Public, Protected, Private. 
# Public memebers: who can be accessed from inside the class, outside the class or from other modules. 
# Protected members: protected memebers are variables or methods that are intended to be accessed only within the class and its sub-class. They are not strictly private but should be treated as internal. naming convention:  _variable (underscore then variable). Use of this is limited in python.  
# Example:
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self._age = age 

# class Sub_employee(Employee):
#     def show_age(self):
#         print("age:", self._age)

# E1 = Sub_employee("Farzana", 45)
# print("Emploee name is:", E1.name) 
# E1.show_age() 

# private memebrs: Private members are variables or methods that cannot be accessed directly from outside the class. they are used to restrict access and protect internal data. in python private memebrs are definned with __ (double underscore or prefix). 

# Getter and setter method: 

# class Student:
#     def __init__(self,name):
#         self.name = name 
#         self.__grade = "B" #private atribute

#     #getter method
#     def get_grade(self):
#         return self.__grade 
    
#     #setter method
#     def set_grade(self,new_grade):
#         grades = ["A", "B", "C", "D", "E", "F"]
#         if new_grade in grades:
#             self.__grade = new_grade
#         else:
#             print("Invalid grade")

# S1 = Student("Farzana")
# print("Name of the student is:", S1.name)
# print("Old grade:", S1.get_grade())
# S1.set_grade("A")
# print("New grade:", S1.get_grade())

# Abstraction: Data abstraction means showing only the Essential features and hiding the complex internal details. In python, abstraction is used to hide the implementation details from the users and expose only necessary parts making the code simpler and easier to intarect with.

#Abstract base class: An Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its sub-classes. It cannot be instantiated directly and serves as a blue print for other classes. 
#Example:
# from abc import ABC, abstractmethod
# class Greet(ABC):  #Abstract Base Class(ABC)
#     @abstractmethod #declaration anotation convention 
#     def say_hello(self):
#         pass 

# class English(Greet):
#     def say_hello(self):
#         return "Hello"
    
# E1 = English()
# print(E1.say_hello())

# Components of abstraction:
#Abstract methods
#Concrete methods 
#Abstract properties 
#Class Instantiation Rules 

#Abstract methods: Abstract methods are the method declarations without a body defined inside an abstract class. They act as placeholders that force sub-classes to provide their own specific implementation, esuring consistant structure across derived classes. 
# Example:   
# from abc import ABC, abstractmethod
# class Animal(ABC): 
#     @abstractmethod #declaration anotation convention 
#     def make_sound(self):
#         pass

#Concrete methods: Conctete methods are fully implemented methods within an abstract class. sub-classes can inherit and use them directly, promoting code reuse without needing to redefine common functionality. 
# Example:  
# from abc import ABC, abstractmethod
# class Animal(ABC): 
#     @abstractmethod #declaration anotation convention 
#     def make_sound(self):
#         pass

#     def move(self):    #it is a concrete method which has implementation 
#         return "moving" 


#Abstract properties: abstract properties work like abstract methods but are used for properties. These properties are declared with "@property" decorator and marked as abstract using @abstractmethod. sub-classes must implement these properties. 
#example:

# from abc import ABC, abstractmethod
# class Animal(ABC): 
#     @property
#     @abstractmethod #declaration anotation convention 
#     def species(self):
#         pass #abstract property, sub-class should be implemented this part. 

# class Dog(Animal):
#     @property 
#     def species(self):
#         return "Canine" 

# d1 = Dog()
# print(d1.species)

#Class Instantiation Rules: abstract classes can not be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations. Attempting to instantiate an abstract class results in a type error.  
#Example: 

# from abc import ABC, abstractmethod
# class Animal(ABC): 
#     @abstractmethod #declaration anotation convention 
#     def species(self):
#         pass 
# a1 = Animal()





