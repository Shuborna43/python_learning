#file handling with read mode- it will retun as strings 

# file = open("book.txt", "r") #to open file, read only
# print(file)
# content = file.read() #to read 
# print(content) #to print
# file.close()



#alternative way: don't need to close manually: it will retun as strings  
# with open("book.txt", "r") as file: #to open the file
#     content = file.read() #to read 
#     print(content) #to print



#another way to read the content of a file by using the readlines(), output returns as list
# with open("book.txt","r") as file:
#     content = file.readlines()
#     print (content)



# using for loop in list with strip()
# with open("book.txt","r") as file:
#     for line in file.readlines():
#         print(line.strip())



#write mode creates a new file or overwrites it entirely if it already exists 
# file = open("book.txt","w")
# file.write("We live in Dhaka\nI have completed BBA\nI love travelling\n")
# file.close()
# f = open("book.txt","r")
# content = f.read()
# print (content)

#write mode creates a new file and add content
# file = open("new_book.txt","w")
# file.write("We live in Chittagong\nI have completed GIS\nI love eating\n")
# file.close()
# f = open("new_book.txt","r")
# content = f.read()
# print (content)

#append mode adds new lines with the existing content
# file = open("book.txt","a")
# file.write("Wadi is innocent\nAdyan is jolly\nI love both\n")
# file.close()
# f = open("book.txt","r")
# content = f.read()
# print (content)

#x method: create a new file or give an error if a file is already existing 
# file = open("book.txt","x")
# file.write("Wadi is innocent\nAdyan is jolly\nI love both\n")
# file.close()

# file = open("new_2_book.txt","x")
# file.write("Wadi is innocent\nAdyan is jolly\nI love both\n")
# file.close()

#r+ mode: it can read and write at a time 
# file = open("book.txt","r+")
# #print(file.read())
# file.write("Wadi studies a lot\nAdyan plays a lot\nI appreciate both\n")
# print(file.read())
# file.close()

file = open("book.txt","r")
content = file.read()
print (content)





 