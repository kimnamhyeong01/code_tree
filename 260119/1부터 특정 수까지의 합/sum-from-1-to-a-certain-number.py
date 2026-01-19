n = int(input())
def mod(n):
    total = 0
    for i in range(n):
        total += i + 1
    return int(total // 10)
print(mod(n))