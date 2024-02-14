m = int(input())
n = int(input())
l = []

for i in range(m, n + 1) :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0 :
            count += 1
            if count > 2 :
                break
    if count == 2 :
        l.append(i)

if l :
    print(sum(l))
    print(l[0])
else :
    print(-1)