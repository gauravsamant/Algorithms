import random
import time
import math

class Sort:
    def selection_sort(self, arr, key=None):
        count = 0
        round = 0
        # print(f'Original array: {arr}')
        for i in range(len(arr)):
            count += 1
            round += 1
            lowest_element_index = i
            for j in range(i+1, len(arr)):
                count += 1
                if arr[j] < arr[lowest_element_index]:
                    lowest_element_index = j
                    # print(f'low found at {j} value is {arr[j]}')
            
            arr[i], arr[lowest_element_index] = arr[lowest_element_index], arr[i]

            # Printing after each iteration of outer for
            # print(f'The array after {round} rounds is {arr}')

        # print(f'Final sorted array is {arr} and took {count} iterations.')
        return (arr, count, round)
    
    def insertion_sort(self, arr, key=None):
        count = 0
        round = 0
        length_of_array = len(arr)
        # print(f'Original array: {arr}\n')
        for ind in range(1, length_of_array):
            count += 1
            round += 1
            current_value = arr[ind]
            position = ind
            # print(f'Current Value: {current_value}, Current Position: {position}, Left Value: {arr[position - 1]}\n')
            while position > 0 and arr[position - 1] > current_value:
                # print(f'High found at lower index {position - 1} having value {arr[position-1]}, current value is {current_value}.\n')
                count += 1
                arr[position] = arr[position - 1]
                position -= 1
                
            arr[position] = current_value
            # Printing after each iteration of outer for
            # print(f'The array after {round} rounds is {arr}.\n\n\n')
        
        # print(f'Final sorted array is {arr} and took {round} steps and {count} iterations.')
        return (arr, count, round)

    def bubble_sort(self, arr, key=None):
        count = 0
        passes = 0
        length_of_array = len(arr)
        # print(f'Original array: {arr}\n')
        for rounds in range(length_of_array - 1, 0, -1):
            count += 1
            passes += 1
            for position in range(rounds):
                current_value = arr[position]
                # print(f'Current Position: {position}. \n')
                if arr[position] > arr[position + 1]:
                    # print(f'Current Value: {current_value}, Current Position: {position}, Right Value: {arr[position + 1]}\n')
                    # print(f'Low found at higher index {position + 1} having value {arr[position + 1]}, current value is {current_value}.\n')
                    count += 1
                    arr[position], arr[position + 1] = arr[position + 1], arr[position]
                
            # arr[position] = current_value
            # Printing after each iteration of outer for
            # print(f'The array after {passes} passes is {arr}.\n\n\n')
        
        # print(f'Final sorted array is {arr} and took {passes} passes and {count} iterations.')
        return (arr, count, passes)
    
    def shell_sort(self, arr, key=None):
        count = 0
        passes = 0
        length_of_array = len(arr)
        # print(f'Original array: {arr}\n')

        # calculate gap
        gap = length_of_array // 2
        while gap > 0:

            passes += 1
            current_ind = gap
            # print(f'No of passes: {passes}, Gap: {gap}, Current Index: {current_ind}')
            while current_ind < length_of_array:
                count += 1
                current_value = arr[current_ind]
                left_ind = current_ind - gap
                while left_ind >= 0 and arr[left_ind] > current_value:
                    count += 1
                    arr[left_ind + gap] = arr[left_ind]
                    left_ind -= gap
                arr[left_ind + gap] = current_value
                current_ind += 1
            gap = gap // 2
            # Printing after each iteration of outer for
            # print(f'The array after {passes} passes is {arr}.\n\n\n')
        
        # print(f'Final sorted array is {arr} and took {passes} passes and {count} iterations.')
        return (arr, count, passes)

    def radix_sort(self, arr):
        count_a = 0
        count_b = 0
        passes = 0
        length_of_array = len(arr)
        max_element = max(arr)
        max_digits = len(str(max_element))
        temp_array = []
        bins = [temp_array] * 10
        # print(bins)

        # print(f'Original array: {arr}\n')
        for power in range(max_digits):
            passes += 1
            for index in range(length_of_array):
                count_a += 1
                least_significant_digit = int((arr[index] / pow(10, power)) % 10)

                if len(bins[least_significant_digit]) > 0:
                    bins[least_significant_digit].append(arr[index])
                else:
                    bins[least_significant_digit] = [arr[index]]
                # print(f'Pass: {passes}, Count: {count_a}')
                # print('Bin is:')
                # for ind, ele in enumerate(bins):
                    # print(f'Index: {ind} ---- Element(s): {ele}')

            kth_index = 0

            for index in range(10):
                if len(bins[index]) > 0:
                    count_b += 1
                    for _ in range(len(bins[index])):
                        arr[kth_index] = bins[index].pop(0)
                        kth_index += 1
                        # print(f'Writing array: {arr}')
        count = count_a + count_b
        # print(f'Final sorted array is {arr} and took {passes} passes and {count_a + count_b} iterations for sorting and {count_b} iteration for writing.')
        return (arr, count, passes)

class MergeSort:
    passes = 0
    count = 0
    def sort(self, arr, left, right):
        MergeSort.count += 1
        MergeSort.passes += 1
        if left < right:
            mid = (left + right) // 2
            self.sort(arr, left, mid)
            self.sort(arr, mid+1, right)
            self._merge(arr, left, mid, right)
        return (arr, MergeSort.count, MergeSort.passes)

    def _merge(self, arr, left, mid, right):
        MergeSort.count += 1
        left_ind = left
        mid_ind = mid + 1
        k_index = left

        temp_array = [0] * (right + 1)
        while left_ind <= mid and mid_ind <= right:
            if arr[left_ind] < arr[mid_ind]:
                temp_array[k_index] = arr[left_ind]
                left_ind += 1
            else:
                temp_array[k_index] = arr[mid_ind]
                mid_ind += 1
            k_index += 1

        while left_ind <= mid:
            temp_array[k_index] = arr[left_ind]
            left_ind += 1
            k_index += 1

        while  mid_ind <= right:
            temp_array[k_index] = arr[mid_ind]
            mid_ind += 1
            k_index += 1

        # print(f'Temp Array: {temp_array}')
        
        for ind in range(left, right + 1):
            arr[ind] = temp_array[ind]


# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
	
	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index]
	
	# This loop runs till start pointer crosses
	# end pointer, and when it does we swap the
	# pivot with element on end pointer
	while start < end:
		
		# Increment the start pointer till it finds an
		# element greater than pivot
		while start < len(array) and array[start] <= pivot:
			start += 1
			
		# Decrement the end pointer till it finds an
		# element less than pivot
		while array[end] > pivot:
			end -= 1
		
		# If start and end have not crossed each other,
		# swap the numbers on start and end
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	# Swap pivot element with element on end pointer.
	# This puts pivot on its correct sorted place.
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	# Returning end pointer to divide the array into 2
	return end
	
# The main function that implements QuickSort
def quick_sort(start, end, array):
	
	if (start < end):
		
		# p is partitioning index, array[p]
		# is at right place
		p = partition(start, end, array)
		
		# Sort elements before partition
		# and after partition
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		
# Driver code
array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')
	
# This code is contributed by Adnan Aliakbar


if __name__ == '__main__':
    sort = Sort()

    #############################################################    
    # For testing if insertion sort algorithm is working properly
    #############################################################
    # arr = []
    # for _ in range (10):
    #     arr.append(random.randint(100, 999))
    
    # sort.insertion_sort(arr)

    #############################################################    
    # For testing if bubble sort algorithm is working properly
    #############################################################
    # arr = []
    # for _ in range (10):
    #     arr.append(random.randint(100, 999))
    
    # sort.bubble_sort(arr)

    #############################################################    
    # For testing if shell sort algorithm is working properly
    #############################################################
    # arr = []
    # for _ in range (10):
    #     arr.append(random.randint(100, 999))
    
    # sort.shell_sort(arr)

    #############################################################    
    # For testing if merge sort algorithm is working properly
    #############################################################
    # sort = MergeSort()
    # arr = []
    # for _ in range (10):
    #     arr.append(random.randint(100, 999))
    
    # print(f'Original Array: {arr}')
    # sort.sort(arr, 0, len(arr) - 1)
    # print(f'Sorted Array: {arr}')

    #############################################################    
    # For testing if radix sort algorithm is working properly
    #############################################################
    # arr = []
    # for _ in range (10):
    #     arr.append(random.randint(100, 999))
    
    # print(f'Original Array: {arr}')
    # sort.radix_sort(arr)
    # print(f'Sorted Array: {arr}')


    ###########################################
    # for benchmarking Selection Sort Algorithm
    ###########################################
    # for i in range(1, 5):
    #     arr = []
    #     for _ in range(10**i):
    #         arr.append(random.randint(100, 99999))

    #     tic = time.process_time()
    #     result = sort.selection_sort(arr)
    #     toc = time.process_time()
    #     print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
    #     print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
    #     print(f'\n\n\n')

    ###########################################
    # for benchmarking Insertion Sort Algorithm
    ###########################################
    # for i in range(1, 5):
    #     arr = []
    #     for _ in range(10**i):
    #         arr.append(random.randint(100, 99999))

    #     tic = time.process_time()
    #     result = sort.insertion_sort(arr)
    #     toc = time.process_time()
    #     print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
    #     print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
    #     print(f'\n\n\n')

    ###########################################
    # for benchmarking Bubble Sort Algorithm
    ###########################################
    # for i in range(1, 5):
    #     arr = []
    #     for _ in range(10**i):
    #         arr.append(random.randint(100, 99999))

    #     tic = time.process_time()
    #     result = sort.insertion_sort(arr)
    #     toc = time.process_time()
    #     print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
    #     print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
    #     print(f'\n\n\n')

    ###########################################
    # for benchmarking Shell Sort Algorithm
    ###########################################
    # for i in range(1, 5):
    #     arr = []
    #     for _ in range(10**i):
    #         arr.append(random.randint(100, 99999))

    #     tic = time.process_time()
    #     result = sort.insertion_sort(arr)
    #     toc = time.process_time()
    #     print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
    #     print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
    #     print(f'\n\n\n')


    ###########################################
    # for benchmarking Merge Sort Algorithm
    ###########################################
    # sort = MergeSort()
    # for i in range(1, 5):
    #     arr = []
    #     for _ in range(10**i):
    #         arr.append(random.randint(100, 99999))

    #     tic = time.process_time()
    #     result = sort.sort(arr, 0, len(arr) - 1)
    #     toc = time.process_time()
    #     print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
    #     print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
    #     print(f'\n\n\n')

    ###########################################
    # for benchmarking Radix Sort Algorithm
    ###########################################
    for i in range(1, 5):
        arr = []
        for _ in range(10**i):
            arr.append(random.randint(100, 99999))

        tic = time.process_time()
        result = sort.radix_sort(arr)
        toc = time.process_time()
        print(f'time taken for sorting array of {len(arr)} elements is {toc - tic}.')
        print(f'It took {result[2]} rounds and {result[1]} steps to complete.')
        print(f'\n\n\n')