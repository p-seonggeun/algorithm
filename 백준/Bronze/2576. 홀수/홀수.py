l = []
for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :
        l.append(n)

l.sort()
if l :
    print(sum(l))
    print(l[0])
else :
    print(-1)