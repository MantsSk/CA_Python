import unittest
import datetime
from personal_code import PersonalCode

class TestKodas(unittest.TestCase):

    def setUp(self):
        self.test_code = "33309240063"
        self.kodas = PersonalCode(self.test_code)

    def test_last_4_personal_code(self):
        self.kodas = PersonalCode(self.test_code) # name 'PersonalCode' is not defined
        self.assertEqual(self.kodas.return_last_four(), self.test_code[-4:]) 

    def test_first_4_personal_code(self):
        self.assertEqual(self.kodas.return_first_four(), self.test_code[:4])

if __name__ == '__main__':
    unittest.main()
