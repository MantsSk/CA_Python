# course_date_list = []
import datetime

class Course:

    def __init__(self, name, hours, lesson_length, start_date, cancelled_dates=[]):
        self.name = name
        self.hours = hours
        self.lesson_length = lesson_length
        self.start_date = start_date
        self.cancelled_dates = cancelled_dates

        self.__moving_date = self.start_date

    @property
    def days_count(self):
        return int(self.hours / self.lesson_length)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if value < datetime.date(2022, 1, 1):
            self._start_date = datetime.date(2022, value.month, value.day)
        else:
            self._start_date = value

    def calculate_dates(self):
        course_date_list = []
        while len(course_date_list) < self.days_count:
            weekday = self.__moving_date.isoweekday()
            if weekday in (1, 2, 3, 4):
                if self.__moving_date in self.cancelled_dates:  # lesson cancelled on 05-04
                    self.__moving_date = self.__moving_date + datetime.timedelta(days=1)
                else:
                    course_date_list.append(self.__moving_date)
                    self.__moving_date = self.__moving_date + datetime.timedelta(days=1)
            else:
                self.__moving_date = self.__moving_date + datetime.timedelta(days=3)
        
        return course_date_list

    def return_formatted_day_list(self):
        formatted_list = []
        for day in self.calculate_dates():
            formatted_list.append(day.strftime("%Y - %B - %d - %A"))

        return formatted_list

    def print_info(self):
        for day in self._calculate_dates():
            print(day)
        print(f"Kursas yra {self.name}, jo ilgis yra {self.days_count} dienos")

# cancelled_dates =  [datetime.date(2022, 5, 4), datetime.date(2022, 5, 11)]
# c = Course("Python", 12, 3, datetime.date(2023, 11,28), cancelled_dates)
# c.print_info()
# print("--------")
# c2 = Course("Python", 16, 4, datetime.date(2019,4,28))
# c2.print_info()

