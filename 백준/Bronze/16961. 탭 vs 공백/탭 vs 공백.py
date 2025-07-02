N = int(input())
T = [0] * 367
S = [0] * 367

five = 0
for _ in range(N):
    l = list(input().split())
    c, s, e = l[0], int(l[1]), int(l[2])
    five = max(five, e - s + 1)

    for i in range(s, e + 1):
        if c == 'T':
            T[i] += 1
        else:
            S[i] += 1

one = 0
two = 0
three = 0
four = 0

for i in range(1, 367):
    if T[i] or S[i]:
        one += 1
    two = max(two, T[i] + S[i])

    if T[i] and S[i]:
        if T[i] == S[i]:
            three += 1
            four = max(four, T[i] + S[i])

print(one)
print(two)
print(three)
print(four)
print(five)