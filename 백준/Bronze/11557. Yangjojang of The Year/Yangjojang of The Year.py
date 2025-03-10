T = int(input())
for _ in range(T) :
    l = []
    N = int(input())
    for _ in range(N) :
        l.append(list(input().split()))

    l.sort(key = lambda x : -int(x[1]))
    print(l[0][0])