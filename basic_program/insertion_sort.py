

# list_1 = [11,12,13,5,6]
# list_1 = [11,12,5,13,6]
# list_1 = [11,5,12,13,6]
# list_1 = [5,11,12,13,6]
# list_1 = [5,11,12,6,13]
# list_1 = [5,11,6,12,13]
# list_1 = [5,6,11,12,13]


def insertion_sort(list_1):

    for i in range(1,len(list_1)):
        k_value = list_1[i]    #the current number that needs to be placed in the correct position (target value)
        j= i-1                 #the index of the element just before the target value 
    
    # as long as j can move backward and the previous number is greater than the target, we keep shifting the previous numbers 1 position to the right.
        while j >= 0 and k_value < list_1[j]:
            list_1[j+1] = list_1[j]  #the number is shifted one position to the right. 
            j -= 1    #decrement j by 1 to check further back. 
       
      # after finding the correct empy slot, the target number is place there.   
            list_1[j+1] = k_value   

if __name__ == "__main__": 
    list_1 = [12,11,13,5,6]
    insertion_sort(list_1)
   
    print(list_1)

#insertion_sort = time complexity O(n) and space complexity O(1)


