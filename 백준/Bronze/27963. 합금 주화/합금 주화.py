d1, d2, x = map(int, input().split())

h = max(d1, d2)
l = min(d1, d2)
w = x / 100

d = 1 / (w / h + (1 - w) / l)
print(d)