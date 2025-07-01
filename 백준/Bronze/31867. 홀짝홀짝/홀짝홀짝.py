N = int(input())
K = list(input())
l = [0, 0]
for i in K:
    if int(i) % 2 == 0:
        l[0] += 1
    else:
        l[1] += 1


if l[0] > l[1]:
    print(0)
elif l[0] < l[1]:
    print(1)
else:
    print(-1)