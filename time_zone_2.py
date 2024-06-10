from datetime import datetime
from dateutil import tz

timeMeeting=datetime(2021,7,8,13,35,tzinfo=tz.gettz('Europa/Moscow'))
timeInIreland=timeMeeting.astimezone(tz.gettz('Europe/Dublin'))
timInGermany=timeMeeting.astimezone(tz.gettz('Europe/Berlin'))
timeInSouthAfrica=timeMeeting.astimezone(tz.gettz('Africa/Johannesburg'))
timeInUsa=timeMeeting.astimezone(tz.gettz('America/Los_Angeles'))
print(f'Irish participants will meet at: {timeInIreland}',f'German participants will meet at: {timInGermany}',f'South African participants will meet at: {timeInSouthAfrica}',f'American participants will meet at: {timeInUsa}',sep='\n')