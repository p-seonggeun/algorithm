N = int(input())
mx, my = 9999, 9999
for _ in range(N):
    x, y = map(int, input().split())
    if my > y:
        mx = x
        my = y
print(mx, my)