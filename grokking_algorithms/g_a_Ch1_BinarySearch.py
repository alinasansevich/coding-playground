#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:46:24 2021

@author: alina

Code from the book "Grokking Algorithms", 
exercises, examples, my experiments with it, etc.

"""

def binary_search(l, item):
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


my_list = [1, 3, 5, 7, 9]

binary_search(my_list, 3)
binary_search(my_list, -3)

# 1.1: answer = 7
# 1.2: answer = 8



