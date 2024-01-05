#!/usr/bin/env python3
""" Test utils """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """ Test get json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_request_get):
        """ test get json method """
        mock_request_get.return_value.json.return_value = test_payload
        actual_result = get_json(test_url)
        self.assertEqual(test_payload, actual_result)
        mock_request_get.assert_called_once_with(test_url)
