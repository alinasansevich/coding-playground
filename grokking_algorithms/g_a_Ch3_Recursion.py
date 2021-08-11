#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:07:35 2021

@author: alina

Code from the book "Grokking Algorithms", 
exercises, examples, my experiments with it, etc.
"""

def countdown(i):
    """ 
    "Print a countdown starting from number i."
    """
    print(i)
    if i <= 1:
        return # base case
    else:
        countdown(i-1) # recursive case

countdown(9)



def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye()

def greet2(name):
    print("How are you, " + name + "?")

def bye():
    print("OK bye!")

greet('Julian')


def fact(x):
    """
    Return the factorial of number x.
    """
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

fact(3)


