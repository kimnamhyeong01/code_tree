arr = [0] * 10
a, b = map(int, input().split())
arr.insert(0, a)
arr.insert(1, b)
for i in range(2, 10):
    arr[i] = int((arr[i - 2] + arr[i - 1]) % 10) 
for i in range(10):
    print(arr[i], end=' ')