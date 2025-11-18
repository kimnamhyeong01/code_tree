N = int(input())
arr = list(map(int, input().split()))
arr.reverse()
for i in range(N):
    if arr[i] % 2 == 0:
        print(arr[i], end=' ')
    else:
        continue