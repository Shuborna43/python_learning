# #dictionaly can be called "map". 
# #A dictionary is an object, it stores unordered collection of data
# #each element has two parts a "key" and a "value"
# #list element has an index and dictionary value has a key. 
# #Elements are commonly refered to as items, or as key-value pairs. 

# students = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
# print(students)
# print(students["A003"])

# #syntax of the four container types
# #Tupple-(value1,value2)
# #list-[value1,value2,value3]
# #set-{value1,value2,value3}
# #dictionary-{"key-1":"value1","key-2":"value2"}

# #access value by using square brackets 
# student_name = students["A002"]
# print(student_name)

# #using the get()
# student_name_1 = students.get("A002")
# print(student_name_1)

# student_name_2 = students.get("A008","Value not found")
# print(student_name_2)

# #square braclets are also used for adding or modifying value 
# students["A002"]="Sorove" #if the value esits in the dictionary, it can not be modified
# print(students)
# students["A002"]="Adyan"
# print(students)
# students["A005"]="Wahida" #if the key does not exist in the dictionary, new Key:value will be added. 
# print(students)

# #del keyword: delete an item with the del keyword and the item's key
# students_group = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
# del students_group["A004"]
# print(students_group)

# #remove all the items of a dictionary using clear()
# students = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
# students_group.clear()
# print(students_group)

# #update by union()
# students.update(students_group)
# print(students)

#pop(): remove and return the key value from the dictionary using the pop(). if a value doesn't exist the specified default is returned.  

# students = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
# person_name = students.pop("A002", "A002 not found")
# print(person_name)
# person_name_1 = students.pop("A009", "A009 not found")
# # print(person_name_1)

# #use the "in" keyword to test for existance of a key in a dictionary 
# if "A002" in students:
#     print(students["A002"]) 
# else:
#     print("A002 is not found")

# print(len(students))

# numbers = {1:"one", 2:"two", 5:"five", 10:"ten", 17:"seventeen", 300:"Three Hundred"}
# numbers [50] = "fifty" #to add a new item in the existing dictionary 
# print(numbers) 

# print(numbers[10])

# if 300 in numbers:  #checks the key by default
#     print(numbers[300])
# else:
#     print("value for 300 is not found")

# if 300 in numbers.keys():  #checks the key 
#     print(numbers[300])
# else:
#     print("value for 300 is not found")



# if "four" in numbers.values(): #directly checks the value 
#     print ("four")
# else:
#     print("four is not found")

#dictionaries:iterating/loop 
# #items()
# students = {1:"Wadi", 2:"Adyan", 3:"Shuborna", 4:"Imran", 5:"Wahida"}
# for student_number, student_name in students.items():
#     # print(f"key is {student_number} and value is {student_name}")
#     print("Key is %s and value is %s" %(student_number,student_name))

#dictionaries:nested loop

numbers = {1:"one", 2:"two", 5:"five", 10:"ten", 17:"seventeen", 300:"Three Hundred"}
students = {1:"Wadi", 2:"Adyan", 3:"Shuborna", 4:"Imran", 5:"Wahida"}
vowels = {"a":"A","e":"E","i":"I","o":"O","u":"U"}

data = {"nums":numbers,"people":students,"vow":vowels} 
print(data)

for element in data:
    our_list = data[element]
    for key,value in our_list.items():
        print("key is %s and value is %s" %(key,value))





