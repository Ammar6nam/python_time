# from datetime import datetime
# from dateutil import tz
# from dateutil.relativedelta import *


# birthday=datetime(1991,7,7,1,20,0,tzinfo=tz.gettz('Germany/Berlin'))
# birthday_NewZealand=birthday.astimezone(tz.gettz('Pacific/Auckland'))
# print(birthday,'  ', birthday_NewZealand)

# timeZone=tz.gettz('Syria/Damascus')
# currentTime=datetime.now(timeZone)
# print(currentTime)


# from datetime import datetime
# from dateutil import tz

# birthday=datetime(1991,7,7,1,20,36,tzinfo=tz.gettz('Asia/Damascus'))
# birthdayInBerlin=birthday.astimezone(tz.gettz('Pacific/Auckland'))

# print(birthday,':',birthdayInBerlin)


from datetime import datetime
from dateutil import tz

myBirthday=datetime(1991,7,7,1,22,26,tzinfo=tz.gettz('Asia/Damascus'))
TimeInAuckland=myBirthday.astimezone(tz.gettz('Pacific/Auckland'))
print(f'My Birthdays time in Damascus was: {myBirthday}',f'and the time in NewZealand"Auckland" was: {TimeInAuckland}',sep='\n')