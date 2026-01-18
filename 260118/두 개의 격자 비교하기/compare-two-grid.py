N, M = map(int, input().split()) 
array1 = []
array2 = []
answer = []
for _ in range(N):
    rows = list(map(int, input().split()))
    array1.append(rows)
for _ in range(N):
    rows = list(map(int, input().split()))
    array2.append(rows)

for i in range(N):
    temp = []
    for j in range(M):
        if array1[i][j] == array2[i][j]:
            temp.append(0)
        else:
            temp.append(1)
    answer.append(temp)

for i in range(N):
    for j in range(M):
        print(answer[i][j], end=' ')
    print()