n, k = map(int, input().split())
commands = [list(map(int, input().split())) for _ in range(k)]
A = []
B = []
block = [0] * n

for i in range(len(commands)):
        A.append(commands[i][0]) 
        B.append(commands[i][1])

length = len(A)
for i in range(length):
    temp1 = 0
    temp2 = 0
    temp1 = A[i] - 1
    temp2 = B[i] - 1
    for j in range(temp1, temp2 + 1):
        block[j] += 1
print(max(block))
# Please write your code here.