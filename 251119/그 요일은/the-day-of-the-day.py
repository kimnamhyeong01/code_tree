m1, d1, m2, d2 = map(int, input().split())
A = input()
month = m1 
date = d1
cnt = 0
day = 0 
week_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 
month_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while month != m2:
    if month == m2:
        break
    if A == week_day[day]:
        cnt += 1
    if date == month_date[month]:
        date = 0
        month += 1
    date += 1
    day += 1
    if day == 6:
        day = 0
 
while date != d2:
    if date == d2:
        break  
    if A == week_day[day]:
        cnt += 1 
    date += 1
    day += 1 
    if day == 6:
        day = 0

if month == m2 and date == d2:
    print(cnt)