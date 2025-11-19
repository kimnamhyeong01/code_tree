n = int(input())
nums = list(map(int, input().split()))
nums.sort()
max_sum = 0
for _ in range(n):
    temp = [] 
    k = len(nums)
    temp.append(nums[0] + nums[k - 1])
    if temp[0] >= max_sum:
        max_sum = temp[0]
    nums.pop(0)
    nums.pop()
print(max_sum)
