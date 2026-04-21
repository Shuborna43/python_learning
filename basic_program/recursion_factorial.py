# def factorial(n):
#     if n == 0: #base case 
#         return 1
#     else:
#         return n * factorial(n-1) #recursive case 

# print(factorial(5)) 

# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1*factorial(0)
# 5*4*3*2*1*1


def f(n):
    if n == 0:
        return 0
    return n + f(n-1)

# print(f(3))

# # 3+factorial(2)
# # 3+2+factorial(1)
# # 3+2+1+factorial(0)
# # 3+2+1+0 



def f(n):
    if n == 0:
        return 1
    return f(n-1) + 1

print(f(5))

f(5): f(4)+1
f(4): f(3)+1+1 = f(3)+2
f(3): f(2)+2+1 = f(2)+3
f(2): f(1)+1+3 = f(1)+4
f(1): f(0)+1+4 = f(0)+5
f(0): 1+5 


