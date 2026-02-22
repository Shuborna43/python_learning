# reference is also known as pass-by-assignment 
# When we call a function, python assings the values we pass into new local variables inside the function. 
# immutable types: int, str, tupple -> can not be changed in place. So reassignment inside a function doesn't affect the original. 
# mutable types: list, dict, set -> can be changed in place. So changes can affects the original object.

# Example of immutable object:
# def increments(counter):
#     counter += 1

# counter = 7
# increments(counter)
# print(counter)



# def increments():
#     global counter
#     counter += 1

# counter = 7
# increments()
# print(counter)



#Example of mutable object:

# def add_item(my_list):
#     my_list.append(8)

# my_list_1 = [5,6,3,2]
# add_item(my_list_1)
# print(my_list_1)

# def add_item(my_list):
#     my_list = [0,0,0]
#     print(my_list)

# my_list_1 = [5,6,3,2]
# add_item(my_list_1)
# print(my_list_1)

def format(first_name, last_name):
    full_name = first_name + " " +last_name
    return full_name 

print(format("Farzana","Khan"))
print(format(first_name = "Farzana",last_name = "Khan"))



