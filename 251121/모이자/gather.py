n = int(input())
A = list(map(int, input().split()))

min_sum = 0
total = 0 
arr = []

for i in range(n):
    total = 0
    for j in range(n):
        total += abs((j - i) * A[j])
    arr.append(total)
    min_sum = min(arr)
print(min_sum)
