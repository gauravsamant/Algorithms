import calendar as cal
import datetime

def day_difference(year):
    # find out what is number of days between thanksgiving and christmas
    # thanksgiving always falls on 4th thrusday of november

    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]

    print(f'thanksgiving is on {thanksgiving}')    
    # thanksgiving_date = datetime.date(year, 11, thanksgiving)

    # christmas_date = datetime.date(year, 12, 25)

    # print(f'Thanksgiving:{thanksgiving_date}')
    # print(f'Christmas Date: {christmas_date}')

    print(f'Differnce between christmas and thanksgiving is: {datetime.date(year, 12, 25) - datetime.date(year, 11, thanksgiving)}')

day_difference(2022)