#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:10:34 2021

@author: alina

Code from the book "Grokking Algorithms", 
exercises, examples, my experiments with it, etc.
"""

# 4.1
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


sum([1])
sum([1, 2])
sum([1, 2, 3, 4, 5])

# 4.2
def how_many(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + how_many(arr[1:])


how_many([1])
how_many([1, 2])
how_many([1, 2, 3, 4, 5])



# 4.3 my answer...

l = [1, 2, 3, 9, 8, 7, 4, 5, 6,]

def find_max_num(l):
	'''
	Return the max value in a list of integers.
	'''
	max_num = l[0]
	for i in range(1, len(l)):
		if l[i] > max_num:
			max_num = l[i]
	return max_num

find_max_num(l)

# ...and the book's answer
def max(l):
	if len(l) == 2:
		return l[0] if l[0] > l[1] else l[1]
	sub_max = max(l[1:])
	return l[0] if l[0] > sub_max else sub_max

max(l)


# 4.4
def binary_search(l, item): # iterative
    """
    (list, int) -> int / None
    Binary search algorithm.
    Returns the index of item in list l, or None if item is not in list.
    """
    low = 0
    high = len(l) - 1
    
    # while you haven't narrowed it down to one element...
    while low <= high:
        # ...check the middle element
        mid = (low + high) // 2
        guess = l[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


l = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

## # from: https://stackoverflow.com/questions/19989910/recursion-binary-search-in-python
## # Base Case: one item (target) in array.
## # Recursive Case: cut array by half each recursive call.
def recursive_binary_search(arr, target):
    mid = len(arr) // 2
    if len(arr) == 1:
        return mid if arr[mid] == target else None
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] < target:
            callback_response = recursive_binary_search((arr[mid:]), target)
            return mid + callback_response if callback_response is not None else None
        else:
            return recursive_binary_search((arr[:mid]), target)


recursive_binary_search(l, 9)
recursive_binary_search(l, 3)
recursive_binary_search(l, -3)



def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))