t = int(input())

for _ in range(t) :
    n = int(input())
    d = [1] * (n + 1)
    d[0] = 0
    if n >= 1 :
        d[1] = 1
    if n >= 2 :
        d[2] = 2
    if n >= 3 :
        d[3] = 4
    if n >= 4 :
        for i in range(4, n + 1) :
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    print(d[n])