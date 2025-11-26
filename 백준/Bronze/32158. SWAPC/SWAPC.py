s = int(input())
S = input().rstrip()
p, c = [], []

for index, i in enumerate(S):
    if i == 'P':
        p.append(index)
    if i == 'C':
        c.append(index)

S = list(S)
for a, b in zip(p, c):
    S[a], S[b] = S[b], S[a]

print(''.join(S))
