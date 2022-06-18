import random
import math
import time

from sort import Sort, MergeSort


class Search:

    def linear_search(self, arr, key):
        count = 0
        for ind, val in enumerate(arr):
            count += 1
            if val == key:
                return (ind, val, count)
        return -1

    def binary_search_iter(self, arr, key):
        sort = Sort()
        count = 0
        left = 0
        right = len(arr) - 1
        array, *_ = sort.radix_sort(arr) #.sort()
        while left <= right:
            count += 1
            mid = (left + right) // 2
            # print(f'Mid: {mid}, Key:{key}, ')
            # print(f'Item: {array[mid]}')
            if array[mid] == key:
                return (mid, key, count)
            elif array[mid] < key:
                left = mid + 1
                continue
            elif array[mid] > key:
                right = mid - 1
        
        return -1

    def binary_search_rec(self, arr, key, count=1):
        sort = Sort()
        # count = 0
        left = 0
        right = len(arr)
        
        if left >= right:
            # print('Left is greater than equal to right, returning....')
            return -1

        # print(f'Original Array is {arr} with length {len(arr)}')
        array, *_  = sort.radix_sort(arr) #.sort()
        
        # print(f'Sorted Array is {array} with length {len(array)}')

        # count += 1
        mid = (left + right) // 2
        # print(f'Mid: {mid}, Key:{key}, ')
        # print(f'Item: {array[mid]}')
        if array[mid] == key:
            return (mid, key, count)
        elif array[mid] < key:
            return self.binary_search_rec(array[mid + 1:], key, count+1)
            
        elif array[mid] > key:
            return self.binary_search_rec(array[:mid], key, count+1)
    
        return -1


if __name__ == '__main__':
    arr = []
    # for _ in range(10):
    #     arr.append(random.randint(10, 50))

    for _ in range(50000):
        arr.append(random.randint(1, 100000000))


    # print(f'Array is {arr}')

    search = Search()
    key=random.choice(arr)
    print(f'Array has {len(arr)} elements and the key to be searched is {key}.')
    if key in arr:
        print(f'Key {key} is in Array at Index {arr.index(key)}.')
    # for _ in range(100):
    # result = search.linear_search(arr, key)
    # result = search.binary_search_iter(arr, key)
    tic = time.process_time()
    result = search.binary_search_rec(arr, key)
    toc = time.process_time()

    if result == -1:
        print('Key not found in array')
    else:
        # print(f'Result is {result}')
        print(f'key {result[1]} is found at index {result[0]}. The search took {result[2]} steps and {toc - tic} seconds.')