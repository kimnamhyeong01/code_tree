Y, M, D = map(int, input().split())

def yoonyeon(y):
    if y % 4 != 0:
        return 0
    elif y % 4 == 0 and y % 100 == 0 and y % 400 != 0:
        return 0
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        return 1
    else:
        return 1 

result_year = yoonyeon(Y)

if result_year == 0:
    if M == 1 and D <= 31:
        print('Winter')
    elif M == 2 and D <= 28:
        print('Winter')
    elif M == 3 and D <= 31:
        print('Spring')
    elif M == 4 and D <= 30:
        print('Spring')
    elif M == 5 and D <= 31:
        print('Spring')
    elif M == 6 and D <= 30:
        print('Summer')
    elif M == 7 and D <= 31:
        print('Summer')
    elif M == 8 and D <= 31:
        print('Summer')
    elif M == 9 and D <= 30:
        print('Fall')
    elif M == 10 and D <= 31:
        print('Fall')
    elif M == 11 and D <= 30:
        print('Fall')
    elif M == 12 and D <= 31:
        print('Winter') 
    else:
        print('-1')
else:
    if M == 1 and D <= 31:
        print('Winter')
    elif M == 2 and D <= 29:
        print('Winter')
    elif M == 3 and D <= 31:
        print('Spring')
    elif M == 4 and D <= 30:
        print('Spring')
    elif M == 5 and D <= 31:
        print('Spring')
    elif M == 6 and D <= 30:
        print('Summer')
    elif M == 7 and D <= 31:
        print('Summer')
    elif M == 8 and D <= 31:
        print('Summer')
    elif M == 9 and D <= 30:
        print('Fall')
    elif M == 10 and D <= 31:
        print('Fall')
    elif M == 11 and D <= 30:
        print('Fall')
    elif M == 12 and D <= 31:
        print('Winter') 
    else:
        print('-1')


        

# Please write your code here.