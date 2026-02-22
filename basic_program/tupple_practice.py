#tuple_1 = (1,2,3,4,2,7,9,3,4)
# print (tuple_1)
# print (tuple_1.count(2))
# print (tuple_1.index(2))
# def remove_element(tup,element):#parameter
#     return tuple (x for x in tup if x != element)

# result = remove_element(tuple_1, 2) #argument

# print (result)

# def max_element(tup):#parameter
#     return max(tup), min(tup)
# result = max_element(tuple_1) #argument
# print (result)

# tup_1 = (4,5,7,3,4,9,7)
# tup_2 = (0,8,4,2,3,5,3)

# def merge_tup(tup1,tup2):
#     return (tup1+tup2)
# result = merge_tup(tup_1,tup_2)
# print (result)

#reverse
tuple_2 = (1,2,3,4,2,7,9,3,4)
def reverse_tup (tup):
    return tup[::-1]

result = reverse_tup (tuple_2)
print (result)

