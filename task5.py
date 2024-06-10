from datetime import datetime , timedelta

currentTime=datetime.now()
delta=timedelta(days=15)
newTime=currentTime-delta
finalForm=newTime.strftime('%Y-%m-%d %H:%M:%S')
print(finalForm)
