E, S, M = map(int, input().split())
a, b, c = 0, 0, 0
answer = 0
while True:
    if E == a and S == b and M == c:
        print(answer)
        break
    a += 1
    b += 1
    c += 1
    answer += 1

    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1