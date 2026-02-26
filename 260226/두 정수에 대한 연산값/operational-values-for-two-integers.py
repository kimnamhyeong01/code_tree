a, b = map(int, input().split())
def func(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2 
    arr = []
    arr.append(a)
    arr.append(b)
    return arr
arr = func(a, b)
print(arr[0], arr[1], end=' ')
# Please write your code here.