N = int(input())
S = input()

d = {}

for i in S:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

f1 = True
f2 = True

for i in 'roygbiv':
    if i not in d:
        f1 = False
        break

for i in 'ROYGBIV':
    if i not in d:
        f2 = False
        break

if f1 and f2:
    print("YeS")
elif f1 and not f2:
    print("yes")
elif f2 and not f1:
    print("YES")
elif not f1 and not f2:
    print("NO!")