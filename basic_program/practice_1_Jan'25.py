#1. Write a Python function safe_divide(a, b) that divides a by b.
#If b is zero, raise a ValueError with the message "Division by zero is not allowed." Use a try and except block to handle the exception.



def safe_divide(a,b):
  try:
    if b==0:
        raise ValueError("Division by zero is not allowed.")
    return a/b
  except ValueError as k:
    return str(k) 
  
print (safe_divide(10,7))

# def handle():
#   try:
#      result = safe_divide(10, 0)
#      print("Result:", result)
#   except ValueError as k:
#      print("Error handled:" , k)       
# handle()





#2.Write a function validate_age(age) that takes an age as input. 
# If the age is negative, raise a ValueError with the message "Age cannot be negative." 
# Use try and except to catch this error and return a friendly error message.
        



def validate_age():
    try: 
      age=int(input("input your age:   "))
      if age<0:
        raise ValueError("Age cannot be negative." )
      print("your age is validated")
  
    except ValueError:
      print("Please enter a positive value for age")
validate_age()