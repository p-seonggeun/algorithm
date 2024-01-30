prime_list = []
l = [True] * 10001
l[0] = False
l[1] = False
for i in range(2, 10001) :
    if l[i] :
        prime_list.append(i)
        for j in range(i + i, 10001, i) :
            l[j] = False
set_prime_list = set(prime_list)

t = int(input())

for _ in range(t) :
    n = int(input())
    add = []
    if n // 2 in set_prime_list :
        print(n // 2, n // 2)
    else :
        for i in prime_list :
            if i > n :
                break
            if n - i in set_prime_list :
                if add :
                    if abs(add[1] - add[0]) > abs(n - 2 * i) :
                        add = [i, n - i]
                else :
                    add = [i, n - i]
        print(*sorted(add))