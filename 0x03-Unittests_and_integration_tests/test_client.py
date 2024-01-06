#!/usr/bin/env python3
""" Test client """

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test github org client """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test org method """
        org_object = GithubOrgClient(org_name)
        org_object.org()
        mock_get_json.assert_called_once()
