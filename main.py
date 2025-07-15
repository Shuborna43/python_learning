import utilities
radius = utilities.get_radius()
weight = utilities.get_weight()
height = utilities.get_height()
sideA = utilities.get_length_sideA()
sideB = utilities.get_length_sideB()
area = utilities.calculate_circle_area(radius)
Volume = (4/3) * 3.14159 * (radius ** 3)  
bmi = utilities.calculate_BMI(weight, height)
hypotenuse = utilities.calculate_hypotenuse(sideA, sideB)

print(f"Area of Circle: {area}\nVolume of sphere: {Volume}\nBMI: {bmi}\nHypotenuse:{hypotenuse}")

