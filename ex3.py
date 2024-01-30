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
#   timing the execution of code, such as using the timeit module in python.
#   They then use this information to 
#   optimize code which results in higher performance.

#3. Use a profiler to measure execution time of the program (skip function definitions) [0.25 pt]
#4. Discuss a sample output. Where does execution time go? [0.25 pts]