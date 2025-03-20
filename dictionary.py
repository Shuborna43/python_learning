#dictionaly can be called "map". 
#A dictionary is an object, it stores unordered collection of data
#each element has two parts a "key" and a "value"
#list element has an index and dictionary value has a key. 
#Elements are commonly refered to as items, or as key-value pairs. 

students = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
print(students)
print(students["A003"])

#syntax of the four container types
#Tupple-(value1,value2)
#list-[value1,value2,value3]
#set-{value1,value2,value3}
#dictionary-{"key-1":"value1","key-2":"value2"}

#access value by using square brackets 
student_name = students["A002"]
print(student_name)

#using the get()
student_name_1 = students.get("A002")
print(student_name_1)

student_name_2 = students.get("A008","Value not found")
print(student_name_2)

#square braclets are also used for adding or modifying value 
students["A002"]="Sorove" #if the value esits in the dictionary, it can not be modified
print(students)
students["A002"]="Adyan"
print(students)
students["A005"]="Wahida" #if the key does not exist in the dictionary, new Key:value will be added. 
print(students)

#del keyword: delete an item with the del keyword and the item's key
students_group = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
del students_group["A004"]
print(students_group)

#remove all the items of a dictionary using clear()
students = {"A001":"Wadi","A002":"Adyan","A003":"Shuborna","A004":"Imran"}
students_group.clear()
print(students_group)

#update by union()
students.update(students_group)
print(students)





