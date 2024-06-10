from datetime import datetime , timedelta
currentTime=datetime.now()
delta=timedelta(days=7)
newTime=currentTime+delta
newForm=newTime.strftime('%Y-%m-%d %H:%M:%S')
print(newForm)