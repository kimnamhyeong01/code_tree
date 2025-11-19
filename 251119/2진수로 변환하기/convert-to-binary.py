n = int(input()) 
digit = []
while n > 0:
    digit.append(n % 2)
    n //= 2 
digit.reverse()
for i in digit:
    print(i, end='')
# Please write your code here.