n = int(input())

def codetree(n):
    if n % 2 == 0 and (int(n // 10) + int(n % 10)) % 5 == 0:
        print("Yes")
    else:
        print("No") 
codetree(n)