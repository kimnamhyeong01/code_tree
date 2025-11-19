N, B = map(int, input().split())
digit = []
while True:
    if N < B:
        digit.append(N % B)
        break 
    digit.append(N % B)
    N //= B 
digit.reverse()
for i in digit:
    print(i, end='')
# Please write your code here.