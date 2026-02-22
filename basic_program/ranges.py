#range(range functions create a range type object that represents a sequence of integers with a "strat, end and step") 
#Genral syntax of range:range(start,stop,step)
#usually we use range function with loop 

#number_1=20
#print(list(range(10,30,5)))

#use of range in "for loop":
# for <var> in <variable>:
#   <statement> 

# letters = ["d","h","t","r"]

# for letter in letters:
#     print(letter,end=",")

# my_strings = "banana"

# for letter in my_strings:
#     print(letter)

# marks_1 = (60,40,50,20,10)
# total = 0
# for number in marks_1:
#     print(f"the mark is: {number}")
#     total += number
    
# print(f"The sum of {len(marks_1)} marks is: {total} ")
# average = total/len(marks_1)
# print ("The average number is %.2f" %average)


# for i in range(1,11): 
#     print(i, end=",")

#printing pattern
# max_row = int(input("enter the number of maximum rows:  "))

# for row in range(0,max_row+1):
#     for star in range(row):
#         print("*", end = " ")
#     print() 

car = ["Toyota", "Ford", "Honda"]
country = ["Bangladesh", "India", "Paakistan", "Spain"]
city = ["Dhaka", "Kulna", "Barisal", "Rajshahi", "Kishoreganj"]

all_variables = [car,country,city]
print(all_variables)

for one_list in all_variables:
    for item in one_list:
        print(item)
    print("-------------------")





