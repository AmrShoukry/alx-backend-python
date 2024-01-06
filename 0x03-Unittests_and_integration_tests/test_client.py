#!/usr/bin/env python3
""" Test client """

import unittest
from unittest.mock import PropertyMock, patch
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

    @parameterized.expand([
        ("google", "Found"),
        ("abc", "Not Found")
    ])
    def test_public_repos_url(self, name, value):
        """ Test public repos url """
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = value
            new_obj = GithubOrgClient(name)
            new_obj._public_repos_url
            mock_repos.assert_called_once_with()

    # @parameterized.expand([
    #     ("google", [
    #             {"name": "one"},
    #             {"name": "two"}
    #         ])
    # ])
    # @patch('client.get_json')
    # def test_public_repos(self, name, value, mock_get_json):
    #     """ Test public repos """
    #     with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_repos:
    #         mock_repos.return_value = value
    #         new_obj = GithubOrgClient(name)
    #         new_obj._public_repos_url
    #         mock_repos.assert_called_once_with()
    #     mock_get_json.return_value = value
    #     new_obj.public_repos()
    #     mock_get_json.assert_called_once()
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has license """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)
