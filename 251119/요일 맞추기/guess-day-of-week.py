m1, d1, m2, d2 = map(int, input().split())
num_days = [0, 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 0]
day = 2
num_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = m1 
date = d1

while True:
    if month == m2:
        if date == d2:
            print(num_days[day])
            break
        elif date > d2:
            date -= 1
            day -= 1
            if day == 0:
                day = 7
    elif month > m2:
        if date == 0:
            month -= 1
            date = num_months[month]
            day -= 1
        if day == 0:
            day = 7
        date -= 1
        day -= 1
    elif month < m2:
        if date == num_months[month]:
            month += 1
            date += 1
            day += 1
        if day == 8:
            day = 1
        date += 1
        day += 1
