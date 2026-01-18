array = []
total = 0
for _ in range(4):
    rows = list(map(int, input().split()))
    array.append(rows)
for i in range(4):
    for j in range(4):
        if i > j:
            total += array[i][j] 
        elif i == j:
            total += array[i][j]
print(total)