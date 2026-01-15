matrix = []
for _ in range(3):
    rows = list(map(int, input().split()))
    matrix.append(rows)
for i in range(3):
    for j in range(3):
        print(matrix[i][j] * 3, end=' ')
    print()