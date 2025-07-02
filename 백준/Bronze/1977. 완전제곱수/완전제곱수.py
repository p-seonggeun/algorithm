M = int(input())
N = int(input())

l = []
for i in range(10001):
    if M <= i * i <= N:
        l.append(i * i)

if l:
    print(sum(l))
    print(l[0])
else:
    print(-1)