N = int(input())
rows = []
for i in range(N): 
    rows.append(i + 1)
for _ in range(N):
    for j in range(N):
        print(rows[j], end='')
    print()
    rows.reverse()