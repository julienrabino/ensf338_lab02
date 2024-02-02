import math
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def lin_search(sorted_list, key):
    i = 0
    for i in range(len(sorted_list)):
        if key == sorted_list[i]:
            return i
    return None

def bin_search(list, first, last, key):
    if first<= last:
        mid = math.floor((first+last)/2)
        if(key == list[mid]):
            return mid
        elif (key < list[mid]):
            return bin_search(list, first, mid-1, key )
        elif (key > list[mid]):
            return bin_search(list, mid+1, last, key)
        


def measure_lin_times(sorted_list):
    key =random.choice(sorted_list)
    times =  timeit.repeat(lambda:lin_search(sorted_list,key), number = 100, repeat = 1000)
    return times

def measure_bin_times(sorted_list):
    last_index = len(sorted_list) - 1
    key = random.choice(sorted_list)
    times =  timeit.repeat(lambda:bin_search(sorted_list,0, last_index,key), number = 100, repeat = 1000)
    return times

def average_time(list_of_times):
    total_sum = sum(list_of_times)
    return total_sum / len(list_of_times)

def fit_func(x, a, b):
    return a * np.log2(x) + b

def main():
    list_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

    list_1000 = [i for i in range(1000)]
    list_2000 =  [i for i in range(2000)]
    list_4000 =  [i for i in range(4000)]
    list_8000=  [i for i in range(8000)]
    list_16000= [i for i in range(16000)]
    list_32000 = [i for i in range(32000)]

    average_lin_times = []
    average_bin_times = []

    lin_1000_avg = average_time(measure_lin_times(list_1000))
    bin_1000_avg = average_time(measure_bin_times(list_1000))
    average_lin_times.append(lin_1000_avg)
    average_bin_times.append(bin_1000_avg)


    lin_2000_avg = average_time(measure_lin_times(list_2000))
    bin_2000_avg = average_time(measure_bin_times(list_2000))
    average_lin_times.append(lin_2000_avg)
    average_bin_times.append(bin_2000_avg)

    lin_4000_avg = average_time(measure_lin_times(list_4000))
    bin_4000_avg = average_time(measure_bin_times(list_4000))
    average_lin_times.append(lin_4000_avg)
    average_bin_times.append(bin_4000_avg)

    lin_8000_avg = average_time(measure_lin_times(list_8000))
    bin_8000_avg = average_time(measure_bin_times(list_8000))
    average_lin_times.append(lin_8000_avg)
    average_bin_times.append(bin_8000_avg)


    lin_16000_avg = average_time(measure_lin_times(list_16000))
    bin_16000_avg = average_time(measure_bin_times(list_16000))
    average_lin_times.append(lin_16000_avg)
    average_bin_times.append(bin_16000_avg)

    lin_32000_avg = average_time(measure_lin_times(list_32000))
    bin_32000_avg = average_time(measure_bin_times(list_32000))
    average_lin_times.append(lin_32000_avg)
    average_bin_times.append(bin_32000_avg)


    plt.subplot(1,2,1)
    plt.title('Linear Search')
    slope, intercept = np.polyfit(list_sizes, average_lin_times, 1)
    linevalues = [slope * x + intercept for x in list_sizes]
    plt.scatter(list_sizes, average_lin_times, label='Linear Search', color='green')
    plt.plot(list_sizes, linevalues,'--', label = 'Linear Fit', color = 'black')
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time for Search (s)')
    plt.legend()


    plt.subplot(1,2,2)
    plt.title('Binary Search')
    popt_bin, _ = curve_fit(fit_func, list_sizes, average_bin_times, p0=[1,1])
    plt.scatter(list_sizes, average_bin_times, label='Binary Search', color='green')
    
    plt.plot(list_sizes, fit_func(list_sizes, *popt_bin), '--', color='black', label='Binary Fit')
    plt.yscale('log')
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time for Search (s)')
    plt.legend()
    plt.tight_layout()
    print("The linear model of the linear search function is: t = %.2e * n + %.2e" % (slope, intercept))
    print("The logarithmic model of the binary search function is %.2e * log2(n) + %.2e" % (popt_bin[0], popt_bin[1]))




    plt.show()


    
  
   




if __name__ == "__main__":
    main()









# 4. The linear search method had a linear function while the binary search had
#    a logarithmic function. For linear search, the fitted curve is as follows: 7.75e-07 * n + 4.14e-03.
#    Meanwhile, for binary search, the fitted curve had a function of  1.02e-05 * log2(n) + 2.45e-05. 
#    These values and models were expected based on the search methods' respective 
#    time complexities. Linear search has time complexity of O(n) -- linear, while 
#    binary search has time complexity O(logn) -- logarithmic. These match with the measured
#    values
# 
