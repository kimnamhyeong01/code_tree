n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_continue(a, b):
    lb = len(b)
    la = len(a)
    for i in range(la - lb + 1):
        if a[i:i + lb] == b:
            return ('Yes')
    return ('No')
print(is_continue(a, b))
# Please write your code here.