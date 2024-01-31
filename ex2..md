EXERCISE 2

 1. Interpolation search is better than binary search since you are able to find the position of 
    the target accurately through the knowledge of the distribution and size of data. Since this estimation is based on
    mathematical reasoning, it is found to be more efficient compared to the process of starting the search in the middle of the list.
    Adding on to that, interpolation is ideal for uniformly distributed data.


 2. Since the data is not uniformly distributed, the midpoint calculation may not be accurate, and
    thus, the search method is not as efficient as it should be. This is because interpolation assumes
    that there is a common pattern among the data and it will try to predict the position of the target based on this pattern. 
    If this pattern does not exist, then the calculation of this index will not be correct.

3.  The formula that calculates the midpoint will have to change, as the current formula 
    is based on the assumption that the data is distributed uniformly (y = mx + b).

4.  When the data is unsorted, linear search is the only option as the efficiency of the other two search methods 
    depend on whether the data is organized. 

5.  Linear search may outperform the other two methods when the number of elements is small. This is because splitting the dataset and finding the midpoints may take more steps
    than just searching through the dataset one by one. 

6. Instead of using recursion, the use of a for/while loop may increase performance for binary and interpolation search for small data. This is due to the fact that there will be
   no function calls, which could decrease execution time.  

