# from datetime import datetime
# date_in_string='Feb 14 2021 8:30AM'
# time=datetime.strptime(date_in_string,'%b %d %Y %I:%M%p')
# print(time)


from datetime import datetime

year1='Feb 14 2021 8:30AM'

date=datetime.strptime(year1,'%b %d %Y %I:%M%p')
print(date)