#set is a container object that stores collection of data. All elements are unique. no duplications are allowed. elements in a set are not stored in any particular order. set can be hold of different data types. A set can be created using curly brackets {}. 

# my_set = {"cat",8,9,6,"dog"}
# print (my_set)

#a set can also be created using the built-in set() function 

# my_set = set("12348932221")
# print(my_set)
# my_set = set("rrhiaanfhkllkdr")
# print(my_set)

# # my_set_3 = set(["cat","dog","frog","bird","bird"])
# # print(my_set_3)

# # items can not be accessed in set by refreing to an index.  
# my_set_4 = {"apple", "banana", "Orange"}
# for element in my_set_4:
#     print(element)

# if "apple" in my_set_4:
#     print("apple was found")

# #add() and update()
# #once a set is created, its items can not be changed but entire item can be added or removed.
# my_set_4.add("guava")
# print(my_set_4)

# my_set_4.update({"multa", "jackfruit", "grape"})
# print(my_set_4)
# print(len(my_set_4))
# #remove an item with remove()-> if the item doesn't exist, remove function will raise an error

# # my_set_4.remove("berry")
# # print(my_set_4)
# my_set_4.remove("multa")
# print(my_set_4)

# #remove an item with discard(). if the item exists it will be removed. but if it does not exist, there will be no error message. 
# my_set_4.discard("berry")
# print(my_set_4)

# #clear()-emty set 
# my_set_5 = {"apple", "banana", "Orange"}
# my_set_5.clear()
# print (my_set_5)

# #the "del" keyword will delete the set permanently 
# del my_set_5
# print(my_set_5)

#union() returns a new set that contains all items from the 2 sets being unioned 
my_set_4 = {"apple", "banana", "Orange"}
my_set_6 = {1,2,3,4}
new_set = my_set_4.union(my_set_6)
print(new_set)
#note: this can also be done with the update()

