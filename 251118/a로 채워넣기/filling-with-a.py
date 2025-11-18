a = input()
new_text = ''
n = len(a)
for i in range(n):
    if i == 1:
        new_text += 'a'
    elif i == n - 2:
        new_text += 'a'
    else:
        new_text += a[i]
print(new_text)