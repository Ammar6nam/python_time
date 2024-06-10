from datetime import datetime , timedelta
import calendar
x=datetime.now()
x=datetime(2000,4,23)

print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)

print(x.strftime("%Y"))
print(x.strftime("%M"))
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%U"))
print(x.strftime("%x"))

new_date = x + timedelta(days=22)
new_time = x - timedelta(hours=20)
print(new_date)
print(new_time)

y = datetime.now()
if x == y:
    print("Datetime objects are the same")
else:
    print("well, they aren't the same...")

timeyones=pytz
calendar