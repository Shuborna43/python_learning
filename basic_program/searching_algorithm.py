# linear search algorithm
# linear search algorithm time complexity = O(n).  [O(n)=order of n]
# characteristics: it works in un-ordered list. it works when there is small number of data 

# binary search algorithm
# linear search algorithm 


# linear search algorithm
surovi = [3,5,6,8,9,2]
find_1 = 8

def search(surovi,find_1):
    len_sur = len(surovi)
    #iterate over the array in order to find the key/value x
    for i in range(0,len_sur): 
        if (surovi[i] == find_1):
            return i
    return -1

result = search(surovi,find_1)

if (result == -1): 
  print("the value is not in the array")
else:
  print(f"The element is in {result} no index")
   

   




