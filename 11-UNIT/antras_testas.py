from cmath import exp
import unittest
import datetime
from studentas import Studentas
from unittest import TestCase

class TestKodas(unittest.TestCase):

    validation_credits_list = [(5, 5), (29,29), (-2, 0), (34,30)]  #actual, expected
    zero_credits_List_input = [-2, -4, -101] 
    thirty_credits_List_input = [34, 30, 101] 

    def setUp(self):
        self.studentas = Studentas("Juozas", 44)

    def test_if_right_ammount_of_credits_assigned(self):
        for actual,expected in self.validation_credits_list:
            with self.subTest():
                self.studentas.credits = actual
                self.assertEqual(self.studentas.credits, expected)
   
    def test_if_returned_credits_are_equal_0(self):
        for actual in self.zero_credits_List_input:
            with self.subTest():
                self.studentas.credits = actual
                self.assertGreaterEqual(self.studentas.credits, 0)

    def test_if_credits_are_equal_30(self):
        for actual in self.thirty_credits_List_input:
            with self.subTest():
                self.studentas.credits = actual
                self.assertLessEqual(self.studentas.credits, 30)

if __name__ == '__main__':
    unittest.main()
