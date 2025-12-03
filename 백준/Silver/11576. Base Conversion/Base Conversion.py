A, B = map(int, input().split())
m = int(input())
M = list(map(int, input().split()))
M.reverse()

t = 0
for i in range(m - 1, - 1, -1):
    t += (A ** i) * M[i]

s = []
while t > 0:
    t, r = divmod(t, B)
    s.append(r)

s.reverse()
print(*s)