m1, d1, m2, d2 = map(int, input().split())

month = m1 
days = d1
num_of_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
elapsed_day = 0

while True:
    if month == m2 and days == d2:
        break 
    elapsed_day += 1
    days += 1

    if days > num_of_months[month]:
        month += 1
        days = 0     
print(elapsed_day)