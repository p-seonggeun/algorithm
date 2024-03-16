x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

i = (a // 3)
j = ((b - d) // 2)
k = (c - e)

a1 = i * x1 ** 3
b1 = j * x1 ** 2
c1 = k * x1 ** 1

a2 = i * x2 ** 3
b2 = j * x2 ** 2
c2 = k * x2 ** 1

print((a2 - a1) + (b2 - b1) + (c2 - c1))