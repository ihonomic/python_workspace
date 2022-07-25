#   Unix epoch is a time reference from 12AM January, 1970
import time
import datetime

print('1.', time.time())
#   Better to  time.sleep(1). in a loop than  time.sleep(30). because when started it cannot Keyboard interrupt exception
datetime.datetime.now()  # date-time object from now
datetime.datetime.fromtimestamp(122000)  # takes in seconds as args
datetime.datetime(2015, 10, 31, 0, 0, 0)  # Creating date-time object

# timedelta - is a data type that represent duration of time NOT MOMENT
delta = datetime.timedelta(weeks=1, days=0, hours=10, minutes=9, seconds=8)
print('2.', delta.days, delta.seconds, delta.microseconds)  # (11, 36548, 0)

delta.total_seconds()  # 986948.0

print('3.', str(delta))  # '11 days, 10:09:08'

#   1000 days from now
dt = datetime.datetime.now() + datetime.timedelta(days=500 * 2)

#   Format datetime object - strftime() - string format time method
readable = dt.strftime('%Y/%m/%d %H:%M:%S')
print('4.', readable)
#   Format datetime object - strptime() - string parse time method
print('5.', datetime.datetime.strptime(readable, '%Y/%m/%d %H:%M:%S'))
