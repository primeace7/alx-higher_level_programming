#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        self.sample = [-9, 65, 0, 4, 43, -567]

    def test_max_integer(self):
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer(self.sample), 65)
