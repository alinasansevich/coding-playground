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




