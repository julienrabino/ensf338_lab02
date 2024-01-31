import math
sorted_list = [1000,2000,4000,8000,16000,32000]

def lin_search(sorted_list, key):
    i = 0
    for i in range(len(sorted_list)):
        if key == sorted_list[i]:
            return i
    return

def bin_search(list, first, last, key):
    if first<= last:
        mid = math.floor((first+last)/2)
        if(key == list[mid]):
            return mid
        elif (key < list[mid]):
            return bin_search(list, first, mid-1, key )
        elif (key > list[mid]):
            return bin_search(list, mid+1, last, key)


print(lin_search(sorted_list,4000))
print(bin_search(sorted_list, 0,5, 4000))