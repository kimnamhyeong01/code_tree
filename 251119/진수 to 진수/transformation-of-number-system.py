a, b = map(int, input().split())
n = input()
num = 0
digit = []

for i in range(len(n)):
    num += int(n[i]) * (a ** (len(n) - 1 - i))    

while True:
    if num < b:
        digit.append(num % b)
        break 
    digit.append(num % b)
    num //= b 

digit.reverse()
for i in digit:
    print(i, end='')