a, b = map(int, input().split())
cnt = 0
temp = 0
def is_complete(n):
    if n % 2 != 0 and n % 10 != 5:
        if n % 3 == 0 and n % 9 != 0:
            return 0
        else:
            return 1 
    else:
        return 0
for n in range(a, b + 1):
    temp = is_complete(n)
    cnt += temp
print(cnt)
# Please write your code here.