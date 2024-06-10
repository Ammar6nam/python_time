from datetime import datetime , timedelta
i=0
currentTime=datetime(year=2020,month=1,day=1)
while i<25:
    delta=timedelta(days=i)
    time1=currentTime+delta
    newForm=time1.strftime('%d %B,%Y')
    # print(newForm)
    i+=1






print(f'Hello Friedrich, your rent of 300€ is due on {newForm}')