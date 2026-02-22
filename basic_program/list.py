# #list is a mutable tuple
# #list can be transformed to tuple and vice versa 
# #data of container (list) can be changed 

# letters_1 = ["a","b","c","d"] #list

# #add data in list
# letters_1.append("e")
# print(letters_1)

# #convert list to tuple
# unchangeable_letters_1 = tuple(letters_1)
# print(unchangeable_letters_1)

# digits_1 = (0,1,2,3,4) #tuple

# # convert tuple to list
# changeable_digits_1 = list (digits_1)
# print(changeable_digits_1)

# # add a new list with old list
# changeable_digits_1.extend([5,6,7,8,9,10])
# print (changeable_digits_1)

# #add new data in list from tuple
# changeable_digits_1.extend((11,12,13))
# print (changeable_digits_1)

# letters = ["s","f",3,"j",4,5]
# #pop function: will remove and return the last data of the list 
# print(letters.pop())#for deleting the last index
# print (letters)
# print(letters.pop(0))#for deleting specific index, need to give index number
# print (letters)
# letters.remove("j") #need to give the data which needs to be deleted
# print (letters)

# letters_3 = ["f","g","h",5,8]

# #update: replcing the data
# letters_3[2] = 5
# print (letters_3)

# #insert: to insert specific data to sepcific index
# letters_3.insert(0,"k") #(index,"string"/number)
# print (letters_3)

# #concat
# letter_4 = ["t","y",8,9]
# all_letters = letters_3 + letter_4
# print (all_letters)

# #all_letters = ['k', 'f', 'g', 5, 5, 8, 't', 'y', 8, 9]

# #while loop 
# i = 0
# while i < len(all_letters):
    
#     #print("letter is", all_letters[i])
#     print(f"letter is {all_letters[i]}")
#     i+=1

#Min and Max function in string considers the first letter
countries = ["Bangladesh", "India", "Srilanka", "Pakistan"]
print(min(countries))
print(max(countries))
print (countries.index("India")) #to get the index number
print(countries.count("Bangladesh")) #number of existence of specific data in the list









