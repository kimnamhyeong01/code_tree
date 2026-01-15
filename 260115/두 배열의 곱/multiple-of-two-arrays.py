array1 = []
array2 = []

for _ in range(3):
    rows_1 = list(map(int, input().split()))
    array1.append(rows_1)

for _ in range(3):
    rows_2 = list(map(int, input().split()))
    array2.append(rows_2) 

for i in range(3):
    for j in range(3):
        print(array1[i][j] * array2[i][j], end=' ')
    print()