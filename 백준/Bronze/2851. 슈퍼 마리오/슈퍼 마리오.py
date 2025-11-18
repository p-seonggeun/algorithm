l = []
for _ in range(10):
    l.append(int(input()))

temp1 = 0
temp2 = 0
for index, i in enumerate(l):
    if temp1 >= 100:
        temp2 = temp1 - l[index - 1]
        break
    temp1 += i
else:
    temp2 = temp1 - l[-1]

if abs(100 - temp1) <= abs(100 - temp2):
    print(temp1)
else:
    print(temp2)