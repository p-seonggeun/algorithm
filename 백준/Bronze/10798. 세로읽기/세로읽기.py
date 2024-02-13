l = []
m = 0
answer = ''
for _ in range(5) :
    l.append(list(input()))

for i in l :
    if m <= len(i) :
        m = len(i)

for i in l :
    if m != len(i) :
        for _ in range(m - len(i)) :
            i.append('-')

for i in range(m) :
    for j in range(5) :
        if l[j][i] != '-' :
            answer += l[j][i]

print(answer)