
import calendar
year=int(input('Enter the year: '))
if 0<year<9999:
    x=True
else:
    x=False
    print('Error!')
if x==True:
    if calendar.isleap(year):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')