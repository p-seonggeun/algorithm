l = [i for i in range(1, 21)]
for _ in range(10) :
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    l = l[:a] + list(reversed(l[a:b + 1])) + l[b + 1:]

print(' '.join(map(str, l)))