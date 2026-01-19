a, b, c = map(int, input().split())
def minimum(a, b, c):
    min = 0
    if a <= b and a <= c:
        min = a
    elif b <= a and b <= c:
        min = b
    elif c <= a and c <= b:
        min = c 
    else:
        min = a 
    return min 
print(minimum(a, b, c))