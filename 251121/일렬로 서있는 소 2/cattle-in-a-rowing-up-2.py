N = int(input())
A = list(map(int, input().split()))
cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if A[i] <= A[j] and A[j] <= A[k]:
                cnt += 1
            else:
                continue
print(cnt)
# Please write your code here.