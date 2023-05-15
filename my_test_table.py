import datetime

today = datetime.date(2023, 5, 20)
yest = today + datetime.timedelta(days=1)
print(today, yest)
print(type(today), type(yest))

my_type = ['9:00-9:30', '9:30-10:00', '10:00-10:30', '10:30-11:00']

today = datetime.date(2023, 5, 20)
day = 1
while day != 10:
    next_day = today + datetime.timedelta(days=day)
    day += 1
    for i in range(len(my_type)):
        print(next_day, my_type[i])
