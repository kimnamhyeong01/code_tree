a, b = map(int, input().split())
cnt = 0
def complete(n):
    _cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            _cnt += 1
    if _cnt == 2 and (int(n / 100) + int(n / 10) + int(n % 10)) % 2 == 0:
        return 1
    else:
        return 0
for n in range(a, b + 1):
    temp = complete(n)
    cnt += temp
print(cnt)
# Please write your code here.