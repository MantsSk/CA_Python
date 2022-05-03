import datetime
from dateutil import tz

hours = 480
lesson_length = 4
days = int(hours/lesson_length)

course_date_list = []
cancelled_dates = [
    datetime.datetime(2022,5,4,18,0,0),
    datetime.datetime(2022,5,11,18,0,0),
    # datetime.datetime(2022,5,18,18,0,0),
    # datetime.datetime(2022,5,19,18,0,0),
    # datetime.datetime(2022,5,25,18,0,0)
]

lesson_date = datetime.datetime(2022,4,28,18,0,0)
temp_hours = 0

while len(course_date_list) < days:
    weekday = lesson_date.isoweekday()
    if weekday in (1,2,3,4):
        if lesson_date in cancelled_dates: # lesson cancelled on 05-04
            lesson_date = lesson_date + datetime.timedelta(days=1)
        else:
            course_date_list.append(lesson_date)
            lesson_date = lesson_date + datetime.timedelta(days=1)
    else:
        lesson_date = lesson_date + datetime.timedelta(days=3)


for day in course_date_list:
    print(day.strftime("%Y - %B - %d - %A"))
    