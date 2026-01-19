a, b = map(int, input().split())

def power(a, b):
    total = 1
    for _ in range(b):
        total *= a
    return total 
print(power(a, b))
# Please write your code here.