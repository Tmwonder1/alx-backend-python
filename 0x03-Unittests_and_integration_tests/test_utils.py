#!/usr/bin/env python3
'''Module to test utils file
'''
from parameterized import parameterized
import unittest
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    '''class for testing access_nestd_map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
