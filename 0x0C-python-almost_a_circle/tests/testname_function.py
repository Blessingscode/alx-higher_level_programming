#!/usr/bin/python3
"""Module to contain the test cases for the name function"""

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """We are testing 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Blessing Nwakwuo' work?"""
        formatted_name = get_formatted_name('Blessing', 'Nwakwuo')
        self.assertEqual(formatted_name, 'Blessing', 'Nwakwuo')

    def test_first_last_middle_name(self):
        """Do names like 'Queen Ogechi Obasi' work?"""
        formatted_name = get_formatted_name('Queen', 'Obasi', 'Ogechi')
        self.assertEqual(formatted_name, 'Queen Ogechi Obasi')


if __name__ == '__main__':
    unittest.main()
