binary = input()
num = 0
n = len(binary) 

for i in range(n):
    num = num + int(binary[i]) * (2 ** (n - 1 -i)) 

print(num) 

# Please write your code here.