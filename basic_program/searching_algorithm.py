# linear search algorithm
# linear search algorithm time complexity = O(n).  [O(n)=order of n]
# characteristics: it works in un-ordered list. it works when there is small number of data 

# binary search algorithm
#complexity = [0(log n)=order of log n]
# linear search algorithm 


# linear search algorithm
# surovi = [3,5,6,8,9,2]
# find_1 = 8

# def search(surovi,find_1):
#     len_sur = len(surovi)
#     #iterate over the array in order to find the key/value x
#     for i in range(0,len_sur): 
#         if (surovi[i] == find_1):
#             return i
#     return -1

# result = search(surovi,find_1)

# if (result == -1): 
#   print("the value is not in the array")
# else:
#   print(f"The element is in {result} no index")
   

# binary search algorithm
# using loop

# def binary_search(arr,find_value):
#    low = 0
#    high = len(arr)-1
#    while low <= high:
#       mid = (low+high)//2
# # check if find_value is present at mid 
#       if arr[mid] == find_value:
#          return mid
# # if find_value is greater, ignor left half 
#       elif arr[mid] < find_value:
#          low = mid+1 
# # if find_value is smaller, ignor right half
#       else:
#          high = mid-1 
#    return -1 #if we reach here then the element wasn't present 

# arr = [2,3,4,6,7,9]
# find_value = 10

# result = binary_search(arr,find_value)

# if result != -1:
#    print("element is present at index", result)
# else:
#    print("element is not present at index")

#recursion 

def binary_serach(arr,low,high,find_value): 
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == find_value:
            return mid
        elif arr[mid] > find_value:
            return binary_serach(arr,low,mid-1,find_value)
        else:
            return binary_serach(arr,mid+1,high,find_value)
    else:
        return -1 #when the element is absent 

arr = [4,5,7,9,11,15]
find_value = 19

result = binary_serach(arr,0,len(arr)-1,find_value)

if result != -1:
   print("element is present at index", result)
else:
   print("element is not present at index")
            
   
   




