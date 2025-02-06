# 1.	Part a: User Input and Greeting
# ○	Print the statement: “Enter your first name:”.
# ○	Get the user’s name from the console and save it to a variable called first_name.
# ○	Print the statement: “Hello, <name>”, where <name> is the actual first name entered by the user.

#The user will input his/her name and it will print Hello with the name of the user.

first_name = input("Enter your first name:    ")
print (f"Hello {first_name}")



# 2.	Part b: Integer Operations
# ○	Create a variable called x and assign it the integer value 5.
# ○	Create a variable called y and assign it the integer value 10.
# ○	Create a variable called total and assign it the sum of x and y.
# ○	Print the total in the format: “5 + 10 = 15” using the variables you created above.

x = 5
y = 10
total = x+y
print (f"{x}+{y}={total}")



# 3.	Part c: Floating-Point Operations
# ○	Create a variable called a and assign it the floating-point value 10.5.
# ○	Create a variable called b and assign it the floating-point value 4.0.
# ○	Create a variable called product and assign it to the product of a multiplied by b.
# ○	Print the value of product in the format: “10.5 * 4.0 = 42.0” using the variables you created above.

a=10.5
b=4.0
product=a*b
print (f"{a} * {b}={product}")

# 4.	Part d: Difference Calculation
# ○	Print the difference between product and total (i.e., product - total).
# ○	Convert product to an integer when performing the subtraction.
# ■	Note: You can do this directly within the parentheses of the print() statement.
# ○	Comment: Answer the following question in a comment:
# How is the output different if you don’t convert product to an integer?

difference1=(product)-total
print(f"{int(product)-total} is the difference when product is converted to integer")
print(f"{difference1} is the difference when product is not converted to integer")



# 5.	Part e: Print Without Newline
# ○	Print the string: “This program is done.”, but do NOT permit a newline to be printed at the end.

print ("This program is done.",end= " ")

c=8
d=8
e=c+d
print (e)
# 6.	Part f: Code Structure
# ○	Include at least 4 comments in your code and use whitespace to group related “paragraphs” of code for better readability.
# 7.	Part g: Program End
# ○	Always end your programs with a single blank line.

