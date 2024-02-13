n, m = map(int, input().split())
# 바구니 만들기
l = [0 for _ in range(n + 1)]

# m번 반복하면서 공 넣기
for _ in range(m) :
    i, j, k = map(int, input().split())
    for a in range(i, j + 1) :
        l[a] = k

print(*l[1:])