from datetime import datetime
from datetime import timedelta


datetime_object = datetime.strptime('1518-10-17 00:13', '%Y-%m-%d %H:%M')
#datetime_object + datetime.timedelta(seconds=3)
print(datetime_object)

#da = datetime(1, 1, 1, 12, 24, 59) + datetime(1, 1, 1, 12, 24, 59)
print(datetime_object + timedelta(minutes=1))
print(datetime_object.time() == datetime.strptime('00:13', '%H:%M').time(),
      datetime_object.time(), datetime.strptime('00:13', '%H:%M').time())

print(timedelta(minutes=60) == timedelta(minutes=59) + timedelta(minutes=1))
