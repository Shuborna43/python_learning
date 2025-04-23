# Scope refers to place or where a variable or function can be accessed or used within the code. 
# there are two main types of scope: 
# Global scope: A variable declared outside of any function. Accessible anywhere in the program.
# Local scope or function scope: A variable declared inside a function and only accessible within that function. 

#Example to access local/function scope:   
#Example-1: currect use within scope 
# def greet(name): #strating of the function body.When we create a function body and that time if we accept a value, that is called parameter. Here name is the parameter.   
#     message = "Hello!"+ name
#     return message #to return/pass a value from a function, when the function is called from somewhere. 


# print(greet("Shuborna")) # here Shuborna is argument. 
# print(greet("Surove"))


# result = greet("Shuborna")
# result_2 = result + "I am adding a new line"
# print(result)
# print(result_2)


#Example-2: trying to use message variable outside its scope:

# def greet(name): #strating of the function body.When we create a function body and that time if we accept a value, that is called parameter. Here name is the parameter.   
#     message = "Hello!"+ name
#     return message #to return/pass a value from a function, when the function is called from somewhere. 

# print(message) #output: NameError: name 'message' is not defined

#Example of Global Variable 
#Example-1: 
# first_name = "Farzana"  
# def change_first_name():
#   global first_name 
#   first_name = "Shuborna"


# #print(change_first_name()) 
# change_first_name()
# print(first_name)

#problem solving-1:
# temparature = 44 
# def update_temparature():
#     global temparature
#     temparature = 30
#     return temparature 

# current_temparature = update_temparature()
# increase_temparature = 10 + current_temparature
# print(increase_temparature)

#problem solving-2:
score = 0
def add_points(points):

    global score
    score += points 

def reset_score():
    global score 
    score = 0

add_points(10) 
add_points(15)
print(score)


reset_score() 
print(score)

