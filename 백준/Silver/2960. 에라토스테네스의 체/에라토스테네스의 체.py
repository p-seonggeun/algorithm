n, k = map(int, input().split())
l = []

prime_list = [True] * (n + 1)

for i in range(2, n + 1) :
    if prime_list[i] :
        if i not in l :
            l.append(i)
        for j in range(i + i, n + 1, i) :
            prime_list[i] = False
            if j not in l :
                l.append(j)

print(l[k - 1])