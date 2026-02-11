A = input()

def palindrome(a):
    n = len(a)
    _a = ''
    for i in range(n - 1, -1, -1):
        _a += a[i]
    if _a == a:
        return 'Yes'
    else:
        return 'No'
print(palindrome(A))
# Please write your code here.