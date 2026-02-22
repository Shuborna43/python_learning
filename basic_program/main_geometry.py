import geometry
length = geometry.get_length() 
width = geometry.get_width() 
perimeter = geometry.calculate_rectangle_perimeter(length, width) 
area = round(geometry.calculate_rectangle_area(length, width),2) 



print (f"Rectangle Dimensions:\nLength: {length} meters\nWidth: {width} meters\nPerimeter: {perimeter} meters\nArea:clear {area} square meters")


