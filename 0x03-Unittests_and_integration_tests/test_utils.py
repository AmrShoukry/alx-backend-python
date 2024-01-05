#!/usr/bin/env python3
""" Test utils """

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test class """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, dictionary, access, expected):
        """ test access nested map """
        self.assertEqual(access_nested_map(dictionary, access), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, dictionary, access, expected):
        """ test access nested map exception """
        with self.assertRaises(expected):
            access_nested_map(dictionary, access)
