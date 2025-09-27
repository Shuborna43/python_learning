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
# Improves Modulariry, Scalability and Maitainability.  

# Characteristics of OOP:
# Class, Object, Encapsulation, Polymorphism, Inheritance, Abstruction 

# CLASS: collection of objects. classes are blueprints for creating objects. A class defines a set of attributes/ variables/properties/fields and methods that the created objects (instances). 
# 1. Classes are created by key word "class"  
# 2. attributes are the variables that belongs to a class 
# 3. Attributs are always public and can be accessed using "."

# Object: An object in a specific instance of a class. It holds its own set of data (instance variables) and can invoke methods defined by its class. Multiple objects can be created from the same class, each with its own unique atrributes. 
#1.


# Example: 
# define a class:
class Dog:
    sound_1 = "Bark"  #class attribute 
    color_1 = "black"
    sound_2 = "Ghew"
    color_2 = "white"
    sound_3 = "Mew"
    color_3 = "brown"

dog_1 = Dog() #object creation 
dog_2 = Dog()
dog_3 = Dog()

print(dog_1.sound_1, dog_1.color_1, dog_2.sound_2, dog_2.color_2, dog_3.sound_3, dog_3.color_3) #accessing the class 


