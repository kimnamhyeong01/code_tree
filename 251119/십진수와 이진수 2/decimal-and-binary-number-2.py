N = input()
n = len(N)
num = 0
new = 1
digit = []
for i in range(n):
    num += int(N[i]) * (2 ** (n - 1 - i))
new = num * 17

while True:
    if new < 2:
        digit.append(new % 2)
        break 
    digit.append(new % 2)
    new //= 2
digit.reverse()
for i in digit:
    print(i, end='')