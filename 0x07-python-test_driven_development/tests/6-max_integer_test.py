#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
mx = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([...])"""

    def test_Ascending_list(self):
        "list in ascending order"
        asc = [1, 2, 3, 4]
        self.assertEqual(mx(asc), 4)
        
    def test_Descending_list(self):
        "list in descending order"
        des = [4, 3, 2, 1]
        self.assertEqual(mx(des), 4)

    def tets_not_orderd_list(self):
        "list not ordered"
        list = [2, 1, 4, 3]
        self.assertEqual(mx(list), 4)

    def test_one_element(self):
        "one element in list"
        one = [5]
        self.assertEqual(mx(one), 5)

    def test_negative_floats(self):
        "negative numbers and floats"
        list = [-5.3, -1.8, -4, -2, -1.1]
        self.assertEqual(mx(list), -1.1)

    def test_empty_list(self):
        "empty list"
        empty = []
        self.assertEqual(mx(empty), None)
    
    def test_strings(self):
        "list of strings"
        l_str = ["abc", "cba", "azz"]
        self.assertEqual(mx(l_str), "cba")

    def test_string(self):
        "String"
        str = "ABCXGHZ"
        self.assertEqual(mx(str), 'Z')
    
    def test_empty_string(self):
        "empty string"
        str = ""
        self.assertEqual(mx(str), None)
    