word1 = input()
word2 = input()

word1_arr = list(word1)
word2_arr = list(word2)
word1_arr.sort()
word2_arr.sort()
n = len(word1_arr)
k = len(word2_arr) 
cnt = 0
if n != k:
    print('No')
elif n == k:
    for i in range(n):
        if word1_arr[i] != word2_arr[i]:
            print('No')
            break
        else:
            cnt += 1

if cnt == n:
    print('Yes')
# Please write your code here.
