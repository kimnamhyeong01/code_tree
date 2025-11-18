cnt_3 = 0
cnt_5 = 0
for _ in range(10):
    a = int(input())
    if a % 3 == 0 and a % 5 != 0:
        cnt_3 += 1
        continue
    elif a % 5 == 0 and a % 3 != 0:
        cnt_5 += 1
        continue
    elif a % 5 == 0 and a % 3 == 0:
        cnt_3 += 1
        cnt_5 += 1
        continue 
    else:
        continue
print(cnt_3, cnt_5)