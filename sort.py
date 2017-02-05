"""
Date : 04 - Feb - 2017

Provide Sorting Classes
"""

class InsertionSort:
    def __init__(self, array, type="integer", key="primary", order='normal'):
        self.array = array
        self.type = type
        self.key = key
        self.order = order

    def sort(self):
        num_ele = len(self.array)
        for index, ele in enumerate(self.array):
            if index+1 < num_ele:
                key = self.array[index+1]
                i = index
            while i >= 0 and self.array[i] > key:
                self.array[i+1], self.array[i] = self.array[i], self.array[i+1]
                i = i - 1

        return self.array

class MergeSort:
    def __init__(self, array, type="integer", key="primary", order='normal'):
        self.array = array
        self.type = type
        self.key = key
        self.order = order
        self.theta = []

    def sort(array):
        #initiate base case
        if len(array) == 1:
            return array

        num_ele = len(array)
        p = int(num_ele/2)
        a = array[:p]
        b = array[p+1:]
        alpha = sort(a)
        beta = sort(b)
        if alpha < beta:
            theta.append(alpha)
        else:
            self.theta.append(beta)
        return self.theta


def sort(array):
    #initiate base case
    #if len(array) == 1:
    #    return array
    if len(array) > 1:
        mid = int(len(array)/2)

        left = array[:mid]
        right = array[mid:]
        print(sort(left))
        print(sort(right))

        i, j, k = 0,0,0

        while i < len(left) and j < len(right):
            if array[i] < array[j]:
                array[k], array[i] = array[i], array[k]
                i = i + 1
            else:
                array[k], array[j] = array[j], array[k]
                j = j + 1
            k = k + 1
    return array

a = [5, 2, 4, 6, 1, 3, 13, 1, 11, 19, 36, 67]
ab = sort(a)
print(ab)

