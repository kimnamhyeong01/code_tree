y = int(input())

def yoonnyeon(n):
    if n % 4 != 0:
        return 0
    elif n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        return 0 
    elif n % 4 == 0:
        return 1 
if yoonnyeon(y) == 0:
    print('false')
else:
    print('true')
    