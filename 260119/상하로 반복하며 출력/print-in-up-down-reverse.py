N = int(input())
temp = [0] * N 
array = []
array.append(temp)
idx = 0
rows = []
for i in range(N):
    rows.append(i + 1)
array.pop(0)
rows_reversed = rows[::-1]
for j in range(N):
    if j == 0:
        array.append(rows)
    elif j % 2 == 0:
        array.append(rows)
    else:
        array.append(rows_reversed)
array_t = [list(x) for x in zip(*array)] 
for i in range(N):
    for j in range(N):
        print(array_t[i][j], end='')
    print()


