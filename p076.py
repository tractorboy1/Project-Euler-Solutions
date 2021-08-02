import math

# func(5) = 6
# func(4) = 3
# func(3) = 2
# func(4)=func(3)+1
# func(5)=func(4)+3
# func(6)=func(5)*2

def n_choose_m(n,m):
    return math.factorial(n) / (math.factorial(m)*math.factorial(n-m))
def my_func(n):
    sum = 0
    for i in range(2,n+1):
        sum += n_choose_m(n,i)
    return sum

print(my_func(5))