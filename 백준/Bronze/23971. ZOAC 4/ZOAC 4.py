H, W, N, M = map(int, input().split())

r, c = 0, 0
for i in range(0, W, M + 1) :
    c += 1

for i in range(0, H, N + 1) :
    r += 1

print(r * c)