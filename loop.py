
list_1 = [2, 2, 3, 5, 5, 5, 6,2,6,6,5,4,0]
new_list = []

i=0
z=0


for i in range (0,len(list_1),1):
    flag = False
    for z in range (0,len(new_list),1):
        if list_1[i] == new_list[z]:
           flag = True
       


    if flag == False:
        x=0
        j=0
        while j<len(list_1):
            if list_1[i] == list_1[j]:
                x+=1
            j+=1
        print(list_1[i], "repeats", x, "times")
        new_list.append(list_1[i]) 
        #i+=1
print(new_list) 
  
       


