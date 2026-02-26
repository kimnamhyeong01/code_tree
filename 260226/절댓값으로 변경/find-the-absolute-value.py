n = int(input())
arr = list(map(int, input().split()))

def definite(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = arr[i] * (-1)
    return arr 
temp = definite(arr)
for i in range(n):
    print(temp[i], end=' ')
# Please write your code here.