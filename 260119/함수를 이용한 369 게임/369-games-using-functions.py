a, b = map(int, input().split())
total = 0
def game(b):
    cnt = 0
    if b % 3 == 0:
        cnt += 1 
    else:
        b = str(b)
        for i in b:
            if i == '3' or i == '6' or i == '9':
                cnt += 1
    return cnt 

for i in range(a, b + 1):
    total += game(i)
print(total)
    