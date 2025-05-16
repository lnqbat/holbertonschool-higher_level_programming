#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with a single-element list"""
        self.assertEqual(max_integer([42]), 42)

    def test_all_negative(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        """Test with both positive and negative integers"""
        self.assertEqual(max_integer([-10, 50, 0, -100]), 50)

    def test_repeated_numbers(self):
        """Test with repeated maximum values"""
        self.assertEqual(max_integer([2, 3, 3, 1]), 3)

    def test_floats(self):
        """Test with floats in the list"""
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 3.8]), 3.9)

    def test_mixed_ints_and_floats(self):
        """Test with a mix of integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 2.9]), 3)

    def test_string_list(self):
        """Test with a list of strings (alphabetical order)"""
        self.assertEqual(max_integer(["apple", "banana", "zebra"]), "zebra")
        
