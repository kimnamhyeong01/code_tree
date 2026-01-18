array = []
cnt = 0
for _ in range(4): 
    rows = list(map(int, input().split()))
    array.append(rows)

for i in range(4):
    for j in range(4):
        if array[i][j] % 5 == 0:
            cnt += 1
print(cnt)