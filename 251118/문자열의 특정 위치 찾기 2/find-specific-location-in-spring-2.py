cnt = 0
arr= ['apple', 'banana', 'grape', 'blueberry', 'orange']
a = input()
for i in range(len(arr)):
    temp = ''
    temp += arr[i] 
    if a == temp[2]:
        print(arr[i])
        cnt += 1
        continue 
    elif a == temp[3]:
        print(arr[i])
        cnt += 1
        continue 
    else:
        continue 
print(cnt)
    
