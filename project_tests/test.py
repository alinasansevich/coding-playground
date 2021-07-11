#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 13:26:22 2021

@author: alina

Getting started with unittest (step 1 towards TTD!)

Resources:
https://realpython.com/python-testing/#writing-your-first-test
"""

import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_floats(self):
        """
        Test that it can sum a list of floats.
        """
        data = [0.4, 0.5, 0.1]
        result = sum(data)
        self.assertEqual(result, 1.0)
    
    def test_mix_list(self):
        """
        Test that it can sum a list of integers and floats.
        """
        data = [1 + 2.0 + 3 + 4.0]
        result = sum(data)
        self.assertEqual(result, 10.0)
    
    def test_tuple_int(self):
        """
        Test that it can sum a tuple of integers.
        """
        data = (1, 2, 3)
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions.
        """
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)
    
    def test_bad_type(self):
        """
        Test if it raises an error.
        """
        data = "Testing, testing, 1, 2, 3."
        with self.assertRaises(TypeError):
            result = sum(data)
            
        
if __name__ == '__main__':
    unittest.main()