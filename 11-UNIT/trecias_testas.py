import unittest
import datetime
from kursas import Course

name_list = [('Python', 'Python'), ('Java', 'Java'), ('C#', 'C#')]

class TestDates(unittest.TestCase):
    def setUp(self):
        self.test_code = "33309240063"
        self.kursas = Course("Python", 480, 4, datetime.date(2019,4,28))

    def test_if_returns_correct_name(self):
        for expected, actual in name_list:
            self.kursas.name = expected
            expected_pavadinimas = actual
            self.assertEqual(expected_pavadinimas, self.kursas.name)

    def test_if_day_count_is_correct(self):
        expected_dienu_skaicius = 120
        self.assertEqual(expected_dienu_skaicius, self.kursas.days_count)

    def test_if_day_count_is_longer_than_0(self):
        self.assertGreater(self.kursas.days_count, 0)
    
    def test_if_date_moving_year_forward_works(self):
        expected_data = datetime.date(2022,4,28)
        self.assertEqual(expected_data, self.kursas._start_date)

    def test_if_second_day_is_calculated_correct(self):
        expected_data = datetime.date(2022,5,2)
        actual_data = self.kursas.calculate_dates()[1]
        self.assertEqual(expected_data, actual_data)

    def test_if_second_day_is_calculated_correct_with_cancelled(self):
        self.kursas.cancelled_dates = [datetime.date(2022,5,2)]
        expected_data = datetime.date(2022,5,3)
        actual_data = self.kursas.calculate_dates()[1]
        self.assertEqual(expected_data, actual_data)

    def test_integration_if_second_day_formatted_is_returned_correct(self):
        expected_data = "2022 - May - 02 - Monday"
        actual_data = self.kursas.return_formatted_day_list()[1]
        self.assertEqual(expected_data, actual_data)

if __name__ == '__main__':
    unittest.main()
