n = int(input())
l = list(map(int, input().split()))
d = [1] * n

for i in range(1, n) :
    for j in range(0, i) :
        if l[i] < l[j] :
            d[i] = max(d[j] + 1, d[i])

print(max(d))