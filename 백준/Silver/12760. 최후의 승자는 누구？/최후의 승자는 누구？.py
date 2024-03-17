import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
dictionary = {}
for i in range(n) :
    l.append(sorted(list(map(int, input().split()))))
    dictionary[i] = 0

ma, ma_index = 0, 0

for i in range(m) :
    for j in range(n) :
        if l[j][i] > ma :
            ma = l[j][i]
            ma_index = j

    for j in range(n) :
        if ma == l[j][i] :
            dictionary[j] += 1

answer = []
temp = list(dictionary.items())
temp.sort(key = lambda x : (-x[1], x[0]))
standard = temp[0][1]
for i in temp :
    if i[1] == standard :
        answer.append(i[0] + 1)

print(*answer)