
import datetime #https://docs.python.org/3/library/datetime.html

print(datetime.date.today())

date = datetime.date(2022,10,10)

print(date)
print(date.year)
print(date.month)
print(date.day)

time = datetime.datetime(2022,10,10,19,18,18)

print(time)
print(time.hour)
print(time.minute)
print(time.second)