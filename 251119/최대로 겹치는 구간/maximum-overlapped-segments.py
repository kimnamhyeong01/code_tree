n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]
x1 = []
x2 = []
for i in range(len(segments)):
    x1.append(segments[i][0])
    x2.append(segments[i][1])
max_1 = max(x1)
max_2 = max(x2)
max_final = max(max_1, max_2) 
checked = [0] * (max_final + 1) 
for i in range(len(x1)):
    for j in range(x1[i], x2[i] + 1):
        checked[j] += 1
cnt = 0
for i in checked:
    if i >= 2:
        cnt += 1
print(cnt)    
# Please write your code here.