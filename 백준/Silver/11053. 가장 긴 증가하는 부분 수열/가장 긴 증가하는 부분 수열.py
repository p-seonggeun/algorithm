n = int(input())
l = list(map(int, input().split()))

d = [1] * n

for i in range(1, n) :
    for j in range(0, i) :
        if l[j] < l[i] :
            d[i] = max(d[i], d[j] + 1)

print(max(d))