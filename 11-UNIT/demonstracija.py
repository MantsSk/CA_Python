import unittest
from unittest import TestCase

class TestKodas(unittest.TestCase):

    number_list = [(2, 2), (1000,1000), (5,8), (3000,1000)]
    
    def test_if_numbers_are_equal(self):
        for expected, actual in self.number_list:
            with self.subTest():
                self.assertEqual(expected, actual) # AssertionError: 5 != 8, AssertionError: 3000 != 1000