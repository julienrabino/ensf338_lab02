
# EXERCISE 1/3
# 1. This code computes the nth number of the fibonacci sequence which
#    is the addition of the numbers at (n-1) and (n-2)

# 2. It is not a divide-and-conquer algorithm because the code produces redundant calculations and 
#    is therefore inefficient.


# 3. O(2^n)

# 4.

def func(n):
    fib_list = []
    
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
