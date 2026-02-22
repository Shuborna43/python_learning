import math
def get_radius():
    radius = float(input("Enter the radius of the circle (in meters): "))
    return radius   

def get_weight():
    weight = float(input("Enter the weight of a person (in kilograms): "))
    return weight   

def get_height():
    height = float(input("Enter the height of a person (in meters): "))   
    return height

def get_length_sideA():
    sideA = float(input("Enter length of side A: "))
    return sideA

def get_length_sideB():
    sideB = float(input("Enter length of side B: "))
    return sideB

def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area 

def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    return BMI

def calculate_hypotenuse(sideA, sideB):
    hypotenuse = math.sqrt(sideA ** 2 + sideB ** 2)
    return hypotenuse

