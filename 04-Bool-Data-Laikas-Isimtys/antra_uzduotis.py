import datetime

now = datetime.datetime.now()
print(now)
print(now - datetime.timedelta(days=5))
print(now + datetime.timedelta(hours=8))
print(now.strftime("%Y %m %d, %X"))
