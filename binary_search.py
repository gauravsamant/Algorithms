# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:35:57 2016

@author: GAURAVSAMANT
"""

def binary_search(data, target):
    '''if low > high:
        return False
    '''
    if len(data) == 0:
        return False
        
    high = len(data)-1  
    mid = (high)//2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data[:mid], target)
    else:
        return binary_search(data[mid+1:],target)
        
data = [1,2,3,4,6,7,8,9,10,11,12,13]
print(binary_search(data,23))