n = int(input()) 
digit = []
while True:
    if n < 2:
        digit.append(n % 2)
        break    
    digit.append(n % 2)
    n //= 2 
digit.reverse()
for i in digit:
    print(i, end='')
# Please write your code here.