import datetime
import pytz

#printing today
today = datetime.date.today()
print(today)

#finding age
birthday = datetime.date(2000, 5, 30)
Age = (today - birthday)
print(Age)

#adding a fixed time period
time_period = datetime.timedelta(hours=10)
Age = Age+time_period
print(Age)

print(today.month)
print(today.weekday())
#monday =0 , sunday=6

#hours mins and secs

print(datetime.time(7, 2, 20, 15))
#datetime.date(Y,M,D)
#datetime.time(h,m,s,ms)
#datetime.datetime(both above)

print(datetime.datetime.now()+time_period)

#timezones
date_today = datetime.datetime.now(tz=pytz.UTC)
date_india = date_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(date_india)
