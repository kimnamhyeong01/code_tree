a, b, c = map(int, input().split())

date = 11
hour = 11
min = 11
elapsed_time = 0

while True:
    if date == a and hour == b and min == c:
        break 
    elapsed_time += 1
    min += 1

    if a == 11 and b < 11:
        print(-1)
        break
    elif a == 11 and b == 11 and c < 11:
        print(-1)
        break 

    if min == 60:
        hour += 1
        min = 0

    if hour == 24:
        date += 1
        hour = 0

print(elapsed_time) 
# Please write your code here.