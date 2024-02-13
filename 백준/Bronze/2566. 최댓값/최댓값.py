l = []
m = 0
index = [0, 0]
for i in range(9) :
    l.append(list(map(int, input().split())))

for i in range(9) :
    for j in range(9) :
        if l[i][j] >= m :
            m = l[i][j]
            index = [i + 1, j + 1]

print(m)
print(*index)