#1. What is a profiler, and what does it do? [0.25 pts]

#   Profilers are programs which analyze many aspects of other programs' execution, mainly how often 
#   various parts are executed and for how long, as well as which parts of the program are executed 
#   the most and which ones are the slowest. They create "execution profiles". Profilers can also 
#   analyze CPU or memory, and even the network being used to run a program. They can also analyze 
#   what kind of objects are being created and the space they take up in memory. For python, these 
#   programs introduce some overhead. 

#2. How does profiling differs from benchmarking? [0.25 pts]

#   Benchmarking involves measuring the performance of a program in a particular environment or 
#   platform. One major factor that affects benchmarking is the test environment - the harware
#   and compiler on which the program is run. Another is the software. Benchmarking mainly involves
#   timing the execution of code, such as using the timeit module in python. This information is then
#   used to optimize code which results in higher performance. The main difference between profiling
#   and benchmarking is that profiling is used to determine why a program performs the way it does
#   by analyzing different processes, while benchmarking determines how well a program performs by 
#   timing execution.

#3. Use a profiler to measure execution time of the program (skip function definitions) [0.25 pt]

import timeit
import cProfile

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

pr = cProfile.Profile()
pr.enable()
test_function()
third_function()
pr.disable()
pr.print_stats()


#4. Discuss a sample output. Where does execution time go? [0.25 pts]

# sample output:

#   68 function calls (23 primitive calls) in 7.563 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    55/10    0.000    0.000    0.000    0.000 ex3.py:27(sub_function)
#        1    0.000    0.000    0.000    0.000 ex3.py:34(test_function)
#        1    7.563    7.563    7.563    7.563 ex3.py:40(third_function)
#       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#   The output includes ncalls - the number of calls a method is called, tottime - the time spent in the 
#   function (excluding any time spent in inner functions), and cumtime - the time
#   spent in the function including inner function calls. From this sample output, it is evident that
#   most of the execution time is spent in third_function(), taking an entire 7.5 seconds. The other
#   functions' execution time is under 0.001 seconds.
