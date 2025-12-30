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

# class Person:
#     def __init__(self): 
#         #these are private atributes: 
#         self.__name = "Geeks"
#         self.__age = 10
        
#         #getter method for name:
#     def get_name(self):
#         return self.__name
    
#         #getter method for age:
#     def get_age(self):
#         return self.__age
    
#         #setter method for name:
#     def set_name(self,name):
#         self.__name = name

#         #setter method for age:
#     def set_age(self,age):
#         self.__age = age

# #Object creation 
# person_1 = Person() 
# print(person_1.get_name(), person_1.get_age())   

# #setting new variables with setter():
# person_1.set_name("John")
# person_1.set_age(21)
# print(person_1.get_name(), person_1.get_age())  












# Question:
# Ques 01: 
# Vehicle, Car, and Motorcycle (Inheritance)
# Problem Description

# Create a base class called Vehicle.
# Then create two subclasses Car and Motorcycle that inherit from the Vehicle class.
# Each subclass should have its own implementation of a speed() method.

# Class Requirements

# Parent Class:
# Vehicle
# Attribute: name (String)
# Child Classes:

# Car
# Method: speed() → prints car speed
# Motorcycle
# Method: speed() → prints motorcycle speed

# Output Example:

# Car speed is 120 km/h
# Motorcycle speed is 80 km/h


# class Vehicle:
#     def __init__(self,km):
#         self.km = km 

# class Car(Vehicle):
#     def speed(self):
#         print("Car speed is", self.km)

# class Motorcycle(Vehicle): 
#     def speed(self):
#         print("Motorcycle speed is", self.km)
    
# c = Car("120 km/h")
# c.speed()

# m = Motorcycle("80 km/h")
# m.speed()


# # Question

# 5. Rectangle and Square (Inheritance)
# Problem Description
# Create a class named Rectangle that can calculate area and perimeter.
#  Create another class named Square that inherits from Rectangle.
#  Square should reuse the Rectangle methods.

# Class Requirements
# Rectangle Class:
# Attributes:

# length (int)

# width (int)

# Methods:

# area() → returns area

# perimeter() → returns perimeter

# Square Class:
# Inherits from Rectangle

# Attribute:

# side (int)

# Uses the same value for length and width

# ExampleOutput:
# Rectangle Area: 50
# Rectangle Perimeter: 30
# Square Area: 16
# Square Perimeter: 16


# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width 
#         self.height = height  

#     def area(self):
#         return self.width*self.height 

#     def perimeter(self):
#         return 2*(self.width+self.height) 
    
#     def info(self):
#         print ("Area of Rectangle is:", self.area())
#         print ("Perimeter of Rectangle is:", self.perimeter())

# class Square(Rectangle):
#     def info(self):
#         print ("Area of Square is:", self.area())
#         print ("Perimeter of Square is:", self.perimeter())

# R1 = Rectangle(5,10)
# R1.info()
# S1 = Square(4,4)
# S1.info()


# Question: 6
# Class Requirements
# 1) Book Class
# Represents a single book.
# Attributes
# title (str): book title
# author (str): author name
# is_available (bool): availability status

# Default should be True

# Constructor

# __init__(title, author)

# Sets is_available = True initially

# Methods

# borrow()

# If is_available is True:

# Set is_available = False

# Print: Borrowed: <title>

# Else:

# Print: "Not available"

# return_book()

# Sets is_available = True

# Print: Returned: <title>

# 2) Library Class

# Represents a collection of books.

# Attribute

# books (list): holds multiple Book objects

# Constructor

# __init__() initializes an empty book list

# Methods

# add_book(book)

# Adds a Book object into books

# Print: Book added: <title>

# borrow_book(title)

# Searches the book list for matching title

# If found, call that book’s borrow()

# If not found, print: "Book not found"

# show_books()

# Prints all books with their status:

# Available → "Available"

# Borrowed → "Borrowed"

# Format:

# <title> - <status>

# Expected Output (Example)
# Book added: Clean Code
# Book added: Python Basics
# Borrowed: Clean Code
# Not available
# Returned: Clean Code
# Clean Code - Available
# Python Basics - Available

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author 
        self.is_available = True  

    def borrow(self):
        if self.is_available:
            self.is_available = False 
            print("borrowed:", self.title)
        else:
            print("Not available")
            
    def return_1 (self):
        self.is_available = True 
        print("returned:", self.title)

class Library: 
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Book added:", book.title)

    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return  
            print("Book not found")

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.return_1()
                return  
            print("Book not found")

    def show_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title}-{status}")

# book_1 = Book("Clean Code","Rober C. Martin")
# book_2 = Book("Python Basics","Shurovi Taj")

# library = Library()

# library.add_book(book_1)
# library.add_book(book_2)

# library.borrow_book("Clean Code")
# library.borrow_book("Clean Code")

# book_1.return_book()
# library.show_books()


library = Library()

while True:
    print("\n1. Add books")
    print("2. Borrow books")
    print("3. Return books")
    print("4. Display all books")
    print("5. Exit")

    choice = input("Enter your choice: ") 


    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter the name of the author: ")
        book = Book(title,author)
        library.add_book(book)

    elif choice == "2":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == "3":
        title = input("Enter book title to return: ")
        library.return_book(title)
    
    elif choice == "4":
        library.show_books()
    
    elif choice == "5":
        print ("Exiting Program")
        break 
    else:
        print("Invalid Choice")










        
           




