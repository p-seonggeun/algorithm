from math import sqrt
m = int(input())
n = int(input())
l = []

for i in range(m, n + 1) :
    if i == 1 :
        continue
    count = 0
    for j in range(2, int(sqrt(i)) + 1) :
        if i % j == 0 :
            count += 1
            if count > 2 :
                break
    if count == 0 :
        l.append(i)

if l :
    print(sum(l))
    print(l[0])
else :
    print(-1)