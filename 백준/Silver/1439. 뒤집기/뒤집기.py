S = input().rstrip()
a, b = 0, 0
for i in S.split("0"):
    if i != '':
        a += 1
for i in S.split("1"):
    if i != '':
        b += 1

print(min(a, b))