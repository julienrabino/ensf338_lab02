import timeit
import matplotlib.pyplot as plt
# EXERCISE 1/3
# 1. This code computes the nth number of the fibonacci sequence which
#    is the addition of the numbers at (n-1) and (n-2)

# 2. It is not a divide-and-conquer algorithm because the code produces redundant calculations and 
#    is therefore inefficient.


# 3. Expression for Time Complexity: O(2^n)

# Exercise 1/4
# 4.

def func_4(n):
    fib_dict = {}
    
    if n == 0 or n == 1:
        return n
    
    if n in fib_dict:
        return fib_dict[n]
    
    result = func_4(n-1) + func_4(n-2)
    fib_dict[n] = result
    return result 

#5. Improved Time Complexity: O(n)

#6. 
# Plot for Original Function
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)


input_values = []
original_times = []
for i in range(36):
    elapsed_time1 = timeit.timeit(lambda: func(i), number = 1)
    original_times.append(elapsed_time1)
    input_values.append(i)

plt.scatter(input_values, original_times)
plt.title('Execution Times for Original Function')
plt.xlabel('Inputs for n')
plt.ylabel('Execution Time')
plt.savefig('ex1.6.1.jpg', bbox_inches = 'tight')
plt.close()

# Plot for Improved Function
def improved_func(n):
    fib_dict = {}
    
    if n == 0 or n == 1:
        return n
    
    if n in fib_dict:
        return fib_dict[n]
    
    result = improved_func(n-1) + improved_func(n-2)
    fib_dict[n] = result
    return result 

improved_times = []
for i in range(36):
    elapsed_time2 = timeit.timeit(lambda: improved_func(i), number = 1)
    improved_times.append(elapsed_time2)

plt.scatter(input_values, improved_times)
plt.title('Execution Times for Improved Function')
plt.xlabel('Inputs for n')
plt.ylabel('Execution Time')
plt.savefig('ex1.6.2.jpg', bbox_inches = 'tight')
plt.close()


