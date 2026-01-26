a, o, c = input().split()
a = int(a)
c = int(c)
def operation(a, o, c):
    if o == '+':
        print(a, o, c, '=', a + c, end=' ')
    elif o == '-':
        print(a, o, c, '=', a - c, end=' ')
    elif o == '/':
        print(a, o, c, '=', int(a / c), end=' ')
    elif o == '*':
        print(a, o, c, '=', a * c, end=' ')
    else:
        print ('False')
    return 0
operation(a, o, c)
# Please write your code here.