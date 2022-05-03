import datetime
from zoneinfo import ZoneInfo

z = ZoneInfo('Poland')

now = datetime.datetime.now(tz=z)  
print(now) #2022-05-03 13:24:58.796733+00:00

now_system = datetime.datetime.now() 
print(now_system) #2022-05-03 16:25:32.413386


