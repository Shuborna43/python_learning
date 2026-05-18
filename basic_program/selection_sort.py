# Selection sortig algorithm 
# Time complexity O(n^2), space complexity O(1) 
# disadvantage: it can not handle large data so we use it in case of small set of data 


def selection_sort(list_1): 
    n = len(list_1)

    for i in range(0,n-1):
        # Assume the current position holds the minimum element
        min_index = i
        # Iterate through the unsorted portion to find the actual minimum 
        for j in range(i+1,n):
            if list_1[j] < list_1[min_index]:
                # Update min_index if the smaller element is found 
                min_index = j 
                # Move minimum element to its correct position  
        list_1[i],list_1[min_index] = list_1[min_index],list_1[i]


if __name__ == "__main__":
    list_1 = [64,25,12,22,11] 
    selection_sort(list_1)
    print (list_1)
            