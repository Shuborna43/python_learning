# #Problem: 1
# def found_n_min(min_1,min_n):
#   for i in range (0,len(list_1),1):
#     if list_1[i]>min_1 and list_1[i]<min_n:
#       min_n = list_1[i]
#   return min_n


# list_1 = [3,-4,55,-64,2,9,10,-33,62,-67]

# min_1 = float("inf")

# for i in range (0,len(list_1),1):
#   if list_1[i]<min_1:
#     min_1 = list_1[i]
# print("minimun number is:", min_1)


# min_2 = found_n_min(min_1,min_n=float("inf"))
# print("2nd minimum number is:", min_2)
# min_3 = found_n_min(min_2,min_n=float("inf"))
# print("3nd minimum number is:", min_3)

# print("The sum of 2nd and 3rd minimum numbers is: ", (min_2+min_3))


# #problem:2

# list_1 = [3,-4,55,-64,2,9,10,-33,62,-67]

# min_1 = float("inf")

# for i in range (0,len(list_1),1):
#   if list_1[i]<min_1:
#     min_1 = list_1[i]
# print("minimun number is:", min_1)

# min_2 = float("inf")

# for i in range (0,len(list_1),1):
#   if list_1[i]>min_1 and list_1[i]<min_2:
#     min_2 = list_1[i]
# print("2nd minimum number is:", min_2)

# min_3 = float("inf")
# for i in range (0,len(list_1),1):
#   if list_1[i]>min_2 and list_1[i]<min_3:
#     min_3 = list_1[i]
# print("3rd minimum number is:", min_3)

# print("The sum of 2nd and 3rd minimum numbers is: ", (min_2+min_3))

# #problem:3

# list_1 = [5, 8, 3, 10, 15, 2, 9]
# even_list =[]
# odd_list = []

# i=0
# x=0
# while i<len(list_1):
#   if list_1[i]%2 == 0:
#     even_list.append(list_1[i])
#   else:
#     odd_list.append(list_1[i])
#   x+=1
#   i+=1
# print("even numbers are =", even_list)
# print("odd numbers are =", odd_list)


# #problem:4

# list_1 = [10, 4, 7, 10, 2, 9,7,8,4,3,333]

# #list_1 = [100000,10,10,10,10,-88,-9876]
# x =  float("-inf")
# for i in range(0,len(list_1),1):
#   if x<list_1[i]:
#     x=list_1[i]
# print(x)

# max_2nd = float("-inf")

# for i in range (0,len(list_1),1):
#   if list_1[i]<x and max_2nd<list_1[i]:
#     max_2nd = list_1[i]
# print(max_2nd)


# #problem:5

# list_1 = [10, 4, 7, 10, 2, 9]

# for j in range(len(list_1) - 1):
#   i =  float("-inf")
#   while i<((len(list_1))-1):
#     if list_1[i]>list_1[i+1]:
#       list_1[i],list_1[i+1] = list_1[i+1],list_1[i]
#     i+=1

# print(list_1[i])
# print (list_1)


# j=(len(list_1)-1)
# while j>0:
#   if list_1[j]>list_1[j-1]:
#     print("Second largest number is:", list_1[j-1])
#     break
#   j-=1

# #   problem: 6

# list_1 = [5, 6, 2, 2, 7, 8, 2, 8, 1, 9, 5, 10, 8,5]

# i=0
# while i<len(list_1):
#   print ("i is", list_1[i])
#   j=i+1
#   flag = False
#   while j<len(list_1):
#     print("j is", list_1[j])
#     #x=0
#     if list_1[i] == list_1[j]:
#       # print ("i is", list_1[i])
#       # print("j is", list_1[j])
#       #x+=1
#       flag= True
#       del list_1[j]
#     j+=1
#   if flag==True:
#     del list_1[i]
#   else:
#     i+=1
#   print(list_1)


# # problem:7

# list_1 = [5,6,2,2,7,8,2,8,1,9,5,10,8,5]
# i = 0
# while(i!=len(list_1)):
#   j = 0
#   flag = False
#   while(j!=len(list_1)):
#     if list_1[i]==list_1[j] and j!=i:
#       flag = True
#     j+=1
#   if flag == False:
#     del list_1[i]
#     i-=1
#   i+=1
# print(list_1)

# # problem: 8

# list_1 = [5,6,2,2,3,6,5,7,2,5,6,7,5,5,5,5]
# idx=0
# while(idx!=len(list_1)):
#   i = idx+1
#   while(i!=len(list_1)):
#     if list_1[idx]==list_1[i]:
#       del list_1[i]
#       i-=1
#     i+=1
#   idx+=1




# print(list_1)


# # problem: 9


# for j in range(0,len(list_1),1):
#   for k in range((j+1),len(list_1),1):
#     if list_1[j] == list_1[k]:
#       list_1[k] = "*"
# print(list_1)

# while "*" in list_1:
#     list_1.remove("*")
# print(list_1)


# # problem: 10
# # List of Squares:
# # Create a list that contains the squares of numbers from 1 to 10.

# n=1

# list_square = []

# while n<11:
#   x=n**2
#   n+=1
#   list_square.append(x)
# print(list_square)


# # problem: 11
# list_1 = [5,6,2,2,3,6,7,2,5]
# new_list = []

# for i in range(0,len(list_1),1):
#   flag = False
#   for n in range(0,len(new_list),1):
#     if list_1[i] == new_list[n]:
#       flag = True
#   if flag == False:
#     new_list.append(list_1[i])
# print(new_list)


# def increment(counter):
#     counter = counter + 1
#     print(counter)
    
# counter = 10

# increment(counter)
# print(counter)




list_1 = [1, 2, 3, 4, 5]

j = len(list_1)
i = 0
while i<j:
  list_1.insert(i,list_1[j-1]) 
  i+=1
print(list_1)


k = len(list_1)
while j == k:
  i = 0
  if list_1[i] == list_1[k-1]:
    del list_1[k-1]
  i+=1
  k-=1
print(list_1)


  