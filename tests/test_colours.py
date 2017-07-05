#!/usr/bin/env python3
from modules import colours
import unittest


class TestColoursMethods(unittest.TestCase):

    def test_light_blue(self):
        test_string = 'test'
        self.assertEqual('\033[1;34m{}\033[0m'.format(test_string), colours.light_blue(test_string))

    def test_yellow(self):
        test_string = 'test'
        self.assertEqual('\033[1;33m{}\033[0m'.format(test_string), colours.yellow(test_string))

    def test_white(self):
        test_string = 'test'
        self.assertEqual('\033[1;37m{}\033[0m'.format(test_string), colours.white(test_string))

    def test_coloured(self):
        test_string = 'test'
        colour_string = 'colour'
        self.assertEqual('colour{}\033[0m'.format(test_string), colours.coloured(colour_string, test_string))
