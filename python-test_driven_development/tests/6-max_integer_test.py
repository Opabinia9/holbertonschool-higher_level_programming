#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_standardlists(self):
        '''test a variety of standard inputs'''
        self.assertEqual(max_integer([3,2,1]), 3)
        self.assertEqual(max_integer([1,2,3]), 3)
        self.assertEqual(max_integer([2,3,1]), 3)
        self.assertEqual(max_integer([]), None)
