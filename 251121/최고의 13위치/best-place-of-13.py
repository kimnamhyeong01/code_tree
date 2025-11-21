n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
total = 0 
max_total = 0
for i in range(n):
    for j in range(n - 2):
        total = 0
        total += grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        max_total = max(total, max_total)
print(max_total)
# Please write your code here.