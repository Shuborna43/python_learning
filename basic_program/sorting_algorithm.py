# in-place sorting: doesn't need extra memory. (e.g. bubble sort and insertion sort)
# internal vs external sorting: 
# merge sorting
# stable sorting
# hybrid sorting 
# comparison based sorting-bubblr sort, insertion sort, selection sort, quick sort, merge sort, heap sort
# non-conparison sorting-counting sort, radix sort  



# BUBBLE Sort:
# step 1: adjacent comparison 
# step 2: swapping 
# step 3: repetation/ loop 

def bubble_sort(arr):
    n = len(arr)
    #traverse/iterates through all array elements 
    for i in range(n):
        swapped = False
        #last i elements are already in place 
        for j in range(0,n-i-1):
            # traverse the array from 0 to n-i-1
            # swap, if the element found is greater than the next element  
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True 

        if swapped == False:
            break 

# main function
if __name__ == "__main__":
    arr = [8,6,2,9,1,0,4]
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    
    bubble_sort(arr)
    print("\n")
    print("Sorted Array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()






