def get_length(): 
    length = float(input("Enter the length of the rectangle (in meters): "))
    return length


def get_width():
    width = float(input("Enter the width of the rectangle (in meters): "))
    return width

def calculate_rectangle_perimeter(length, width):
    Perimeter = (2 * (length + width))
    return Perimeter
  

def calculate_rectangle_area(length, width):
    Area = length * width
    return Area
  
 
