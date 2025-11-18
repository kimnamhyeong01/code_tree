n = int(input())
def square(n):
    temp = 1
    for i in range(n):
        for j in range(n):
            if temp == 9: 
                print(temp, end=' ')
                temp = 1 
                continue
            else:
                print(temp, end=' ')
                temp += 1
                continue
        print('')
square(n)
# Please write your code here.