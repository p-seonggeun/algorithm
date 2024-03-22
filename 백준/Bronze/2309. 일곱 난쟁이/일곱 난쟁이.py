s = 0
h = []
ret = []
answer = []
for _ in range(9) :
    h.append(int(input()))
    s += h[-1]

for i in range(9) :
    for j in range(i) :
        if s - h[i] - h[j] == 100 :
            ret = [i, j]
            break

for i in range(9) :
    if i == ret[0] or i == ret[1] :
        continue
    answer.append(h[i])

answer.sort()
for i in answer :
    print(i)