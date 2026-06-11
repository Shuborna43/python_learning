# Quick_sort: this method follows "divide and conquer principle"
# it works in 3 stages: 
# 1. Pivot: one item from the array is considered as main item. it can be anyone but usually the last item is taken as Pivot.
# 2. Smaller nunbers than Pivot is kept in the left side of the pivot and larger nunbers than Pivot is kept in the right side of the pivot.
# 3. Recurssion: it assumes the smaller numbers as one sub array and the larger numbers as another sub array and sort accordingly. 
# time complexity: O (n log n), space complexity: O (log n)
# Example:


# list_1 = [10,7,8,9,1,5]

def partition(list_1,low,high):
    pivot = list_1[high] #choose the pivot
    # index of smaller element and indicates the righ position of pivot found so far 
    
    i = low-1 

    # 
    for j in range(low,high):
        if list_1[j] < pivot:
            i += 1
            swap(list_1,i,j)

    swap(list_1,i+1,high)        
    return i+1

def swap(list_1,i,j):
    list_1[i],list_1[j] = list_1[j],list_1[i]

def quick_sort(list_1,low,high):
    if low < high:
        # pi is the partition return index of the pivot 
        
        pi = partition(list_1,low,high) #pi = pivot value
        #recursion calls for smaller elements and greater of equals elements 
        quick_sort(list_1,low,pi-1)
        quick_sort(list_1,pi+1,high)



if __name__ == "__main__":
    list_1 = [10,7,8,9,1,5]   #[1,5,8,9,10,7]
    n = len(list_1)

    quick_sort(list_1,0,n-1)

    for val in list_1:
        print(val,end = " ") 



