#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:18:29 2021

@author: alina

Getting started with unittest (step 1 towards TTD!)

Resources:
https://realpython.com/python-testing/#writing-your-first-test
"""

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
