# lists of lists
# 
# row_0 = ["a", "b", "c", "d", "e", "f", "g", "h"]
# row_1 = ["i", "j", "k", "l", "m", "n", "o", "p"]
# row_2 = ["q", "r", "s", "t", "u", "v", "w", "x"]
# row_3 = ["y", "z"]
# table = [row_0,
#          row_1,
#          row_2,
#          row_3]
# number_of_rows = len(table)
# i = 0
# while i < number_of_rows:
#     print("Row %d" % (i), end=':: ')
#     number_of_letters_in_this_row = len(table[i])
#     j = 0
#     while j < number_of_letters_in_this_row:
#         print((table[i][j]), end=' ')
#         j+=1
#     print()
#     i+=1

student_name = ["Adyan", "Wadi", "Meraj"]
class_name = [5,6,7,8]
club_name = ["football", "cricket"]

student_data = [student_name, class_name, club_name]
items = ["student_name", "class_name", "club_name"]
len_of_student_data = len(student_data)  

i = 0
while i < len_of_student_data:
    print (f"{items[i]}", end=":: " )

    len_of_each_list = len(student_data[i])
    j=0
    while j < len_of_each_list:
        print (student_data[i][j], end=", " ) 
        j += 1
    print ()
    i +=1



