# 1. Design a Class
# Problem Description
# Design a class named MyClass that contains a public method named display(). This method should print "Hello World" when called.
# Class Requirements
# Class Name: MyClass
# Method:
# Name: display()
# Parameters: none
# Return Type: void (prints output)
# Access Modifier: public
# Body: print "Hello World"
# Example Output
# Hello World
#Answer 1: 
# class MyClass:
#     def display(self):
#         print ("Hello World")

# mc = MyClass()
# mc.display() 

# 2. SalesEmployee (inherits Employee)
# Attributes:
# Inherited: id, salary
# New: sales (int)
# Constructor: __init__(self, id, salary, sales)
# Calls: super().__init__(id, salary)
# Initializes sales

# Example
# Input:
# id = 14, salary = 30000, sales = 20

# Output:
# 14 30000
# 14 30000 20


#Answer 2: 

# class Employee:
#     def __init__(self,id,salary):
#         self.id = id
#         self.salary = salary 
    
    # def print_1(self):
    #     print(self.id,self.salary)


# class SalesEmployee(Employee):
#     def __init__(self, id, salary, sales):
#         super().__init__(id, salary)
#         self.sales = sales 
    
    # def print_2(self):
    #     print(self.id,self.salary,self.sales)

# emp_2 = Employee(14,30000)
# print(emp_2.id,emp_2.salary)
# emp_1 = SalesEmployee(14,30000,20)
# print(emp_1.id,emp_1.salary,emp_1.sales)
# # emp_2.print_1()
# # emp_1.print_2()


# 3. Abstraction in Python
# Problem Description
# Demonstrate abstraction using an abstract class Shape and a concrete class Square.
# Class Requirements
# 1. Shape (Abstract Class)
# Attribute: color (String)

# Constructor: Shape(c) → assigns value to color
# Methods:
# get_color() → returns color
# get_area() → abstract method, returns float
# 2. Square (extends Shape)
# Attribute: side (float)
# Constructor: Square(c, side) → calls super(c) and sets side

# Method:
# get_area() → returns side * side
# Example
# Input:
# color = "red", side = 5.0

# Output:
# red 25.0

#Answer 3: 
# from abc import ABC, abstractmethod
# class Shape(ABC):  #Abstract Base Class(ABC)
#     def __init__(self,c):
#         self.c = c
    
#     def get_color(self):
#         return self.c
    
#     @abstractmethod
#     def get_area(self):
#        pass 


# class Square(Shape):
#     def __init__(self,c,side):
#         super().__init__(c)
#         self.side =side
    
#     def get_area(self):
#         return self.side * self.side

# s1 = Square("red",5.0)
# print (s1.get_color(), s1.get_area())




# 4. Encapsulation in Python
# Problem Description
# Create a Person class that demonstrates encapsulation via private attributes and public getters/setters.
# Class Requirements
# Private Attributes:
# name (String) → default: "Geeks"


# age (int) → default: 10


# Public Methods:
# get_name(), get_age() → getters


# set_name(name), set_age(age) → setters


# Example
# Function Calls:
# Person(), get_name(), set_name("John"), set_age(21), get_name(), get_age()

# Output:
# Geeks John 21

class Person:
    def __init__(self): 
        #these are private atributes: 
        self.__name = "Geeks"
        self.__age = 10
        
        #getter method for name:
    def get_name(self):
        return self.__name
    
        #getter method for age:
    def get_age(self):
        return self.__age
    
        #setter method for name:
    def set_name(self,name):
        self.__name = name

        #setter method for age:
    def set_age(self,age):
        self.__age = age

#Object creation 
person_1 = Person() 
print(person_1.get_name(), person_1.get_age())   

#setting new variables with setter():
person_1.set_name("John")
person_1.set_age(21)
print(person_1.get_name(), person_1.get_age())  