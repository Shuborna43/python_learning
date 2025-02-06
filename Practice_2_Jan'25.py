#3.Write a function read_file(filename) that reads a file and returns its content. 
# Use a try and except block to catch a FileNotFoundError and return the message "File not found."

# def read_file(filename):
#     try:
       
#      with open(filename, "r") as file:
#       readFile = file.read()
#       print(readFile)

#       if filename!=True:
#         return FileNotFoundError

#     except:
#       print ("File not found")


# read_file ("addition.py")


#4.Create a function check_password(password) that raises a custom exception called WeakPasswordError 
# if the password length is less than 8. Use try and except to catch this exception and return an appropriate message.

def check_password():
    
    
    try:
        password=input ("input a password:    ")
        if len(password)<8:
            raise  "password should be longer"
        return password, "is a strong password"
        
        
    except:
        return "WeakPasswordError:please enter the password length more than 8"
    

print (check_password())

        

      





