num = 1
while num != 25:
    num = int(input())
    if num < 25:
        print('Higher')
    elif num > 25:
        print('Lower')
    else:
        print('Good')
        break