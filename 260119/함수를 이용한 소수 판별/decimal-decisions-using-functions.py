a, b = map(int, input().split())
total = 0
def sosu(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return n
    else:
        return 0 

for i in range(a, b + 1):
    total += sosu(i)
print(total)