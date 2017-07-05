#!/usr/bin/env python3
from modules import interactions
import unittest


class TestInteractionsMethods(unittest.TestCase):

    def test_get_banner(self):
        # test that the banner returns a non-empty string
        banner = interactions.get_banner()
        self.assertTrue(len(banner) > 0)

    def test_get_website(self):
        # test that the website_url returns a non-empty string
        website_url = interactions.get_website()
        self.assertTrue(len(website_url) > 0)

    def test_get_github(self):
        # test that the github_url returns a non-empty string
        github_url = interactions.get_github()
        self.assertTrue(len(github_url) > 0)

    def test_get_version(self):
        # test that the version_number returns a non-empty string
        version_number = interactions.get_version()
        self.assertTrue(len(version_number) > 0)

    def test_get_welcome(self):
        # test that the welcome message returns a non-empty string
        welcome_message = interactions.get_welcome()
        self.assertTrue(len(welcome_message) > 0)

    def test_get_confirmation(self):
        # test that the confirmation message returns a non-empty string
        confirmation_message = interactions.get_confirmation()
        self.assertTrue(len(confirmation_message) > 0)
