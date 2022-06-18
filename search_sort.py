class SearchSort:
    def sort(self, arr):
        # length_of_arr = len(arr)
        max_element = max(arr)
        max_digits = len(str(max_element))

        temp_array = []
        bins = [temp_array] * 10

        for power in range(max_digits):
            for _, element in enumerate(arr):
                least_significant_digit = int((element / pow(10, power)) % 10)

                if len(bins[least_significant_digit]) > 0:
                    bins[least_significant_digit].append(element)
                else:
                    bins[least_significant_digit] = [element]
                
            kth_index = 0

            for index in range(10):
                if len(bins[index]) > 0:
                    for _ in range(len(bins[index])):
                        arr[kth_index] = bins[index].pop(0)
                        kth_index += 1

        return arr

    def search(self, arr, key, index_needed=None):
        if index_needed:
            result = self._search_linear(arr, key)
        else:
            arr = self.sort(arr)
            result = self._search_binary(arr, key)

        if isinstance(result, int):
            if result == -1:
                return False
            else:
                return True
        else:
            if isinstance(result, tuple):
                return result

    def _search_binary(self, arr, key):
        left_index = 0
        right_index = len(arr)

        if left_index >= right_index:
            return -1
        
        mid = (left_index + right_index) // 2

        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            return self._search_binary(arr[mid + 1:], key)
        elif arr[mid] > key:
            return self._search_binary(arr[:mid], key)
        
        return -1

    def _search_linear(self, arr, key):
        for ind, val in enumerate(arr):
            if val == key:
                return (ind, val)
        return -1

if __name__ == '__main__':
    import random
    import time

    arr = []

    for _ in range(100):
        arr.append(random.randint(100, 999))
    
    search_sort = SearchSort()

    key1 = random.choice(arr)
    key2 = random.randint(1, 99)

    if key1 in arr:
        print(f'Key {key1} is in array at index: {arr.index(key1)}')

    if key2 in arr:
        print(f'Key {key2} is in array at index: {arr.index(key2)}')
    else:
        print(f'Key {key2} is Not in Array')

    tic1 = time.process_time()
    result1 = search_sort.search(arr[:], key1)
    toc1 = time.process_time()
    if result1:
        print(f'Key1 found in array')
    else:
        print(f'Key1 NOT found in array')
    print(f'Time took for Process 1 {toc1 - tic1}\n\n')

    tic2 = time.process_time()
    result2 = search_sort.search(arr[:], key1, index_needed=True)
    toc2 = time.process_time()
    if result2:
        print(f'Key1 {result2[1]} found in array at {result2[0]}')
    else:
        print(f'Key2 NOT found in array')
    print(f'Time took for Process 2 {toc2 - tic2}\n\n')

    tic3 = time.process_time()
    result3 = search_sort.search(arr[:], key2)
    toc3 = time.process_time()
    if result3:
        print(f'Key2 found in array')
    else:
        print(f'Key2 NOT found in array')
    print(f'Time took for Process 3 {toc3 - tic3}\n\n')

    tic4 = time.process_time()
    result4 = search_sort.search(arr, key2, index_needed=True)
    toc4 = time.process_time()
    if result4:
        print(f'Key2 {result4[1]} found in array at {result4[0]}')
    else:
        print(f'Key2 NOT found in array')
    print(f'Time took for Process 4 {toc4 - tic4}\n\n')