# Simple subtraction program
def subtract_numbers():
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform subtraction
    result = num1 - num2
    
    # Display the result
    print(f"The result of {num1} - {num2} is {result}")

# Call the function
subtract_numbers()