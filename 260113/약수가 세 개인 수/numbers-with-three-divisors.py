a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += 1 
        else:
            continue 
    if total == 3:
        cnt += 1
    else:
        continue
print(cnt)      
