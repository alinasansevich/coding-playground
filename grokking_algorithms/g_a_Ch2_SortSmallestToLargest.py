#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:49:32 2021

@author: alina

Code from the book "Grokking Algorithms", 
exercises, examples, my experiments with it, etc.
"""

def find_smallest(arr):
    """
    (list of int) -> int 
    Returns the smallest integer in a list of integers (I could just use min(list))
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    """ 
    (list of int) -> sorted list
    Returns list arr with elements sorted from smallest to largest.
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

selection_sort([5, 3, 6, 2, 10])