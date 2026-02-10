M, D = map(int, input().split())

def date(M, D):
    if M == 1 and D <= 31:
        return('Yes')
    elif M == 2 and D <= 28:
        return('Yes')
    elif M == 3 and D <= 31:
        return('Yes')
    elif M == 4 and D <= 30:
        return('Yes')
    elif M == 5 and D <= 31:
        return('Yes')
    elif M == 6 and D <= 30:
        return('Yes') 
    elif M == 7 and D <= 31:
        return('Yes') 
    elif M == 8 and D <= 31:
        return('Yes') 
    elif M == 9 and D <= 30:
        return('Yes') 
    elif M == 10 and D <= 31:
        return('Yes') 
    elif M == 11 and D <= 30:
        return('Yes') 
    elif M == 12 and D <= 31:
        return('Yes') 
    else:
        return('No')
print(date(M, D))