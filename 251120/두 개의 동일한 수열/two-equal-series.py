n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
cnt = 0

for i in range(n):
    if A[i] != B[i]:
        print('No')
        break 
    else:
        cnt += 1
    if cnt == n:
        print('Yes')
        break
# Please write your code here.