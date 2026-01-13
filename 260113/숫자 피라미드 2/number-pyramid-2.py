N = int(input())
total = 0
for i in range(1, N + 1):
    for _ in range(i):
        total += 1
        print(total, end=' ' )
    print()