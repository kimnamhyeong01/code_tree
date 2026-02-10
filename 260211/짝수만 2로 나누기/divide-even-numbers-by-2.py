n = int(input())
arr = list(map(int, input().split()))

def div(n):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)
    return 0 
div(n)
for i in range(n):
    print(arr[i], end=" ")
# Please write your code here.