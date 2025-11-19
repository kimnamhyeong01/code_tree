m1, d1, m2, d2 = map(int, input().split())
A = input()

month = m1 
date = d1

cnt = 0
day = 0 
week_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 
month_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if week_day[day] == A:
        cnt += 1
    
    if month == m2 and date == d2:
        break 
    
    date += 1 
    if date > month_date[month]:
        date = 1
        month += 1
    
    day = (day + 1) % 7

print(cnt)