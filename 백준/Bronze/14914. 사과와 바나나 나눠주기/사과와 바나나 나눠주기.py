import math
a, b = map(int, input().split())
g = math.gcd(a, b)

l = []

for i in range(1, g + 1):
    if g % i == 0:
        l.append(i)

for i in l:
    print(i, a // i, b // i)