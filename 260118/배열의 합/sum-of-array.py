array = []
for _ in range(4):
    rows = list(map(int, input().split()))
    array.append(rows)
for i in range(4):
    sum = 0
    for j in range(4):
        sum += array[i][j]
    print(sum)
    