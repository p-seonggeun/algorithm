import sys
input = sys.stdin.readline
N = int(input())

l = [0] + list(map(int, input().split()))
d = {}
for i in range(1, len(l)) :
    for j in range(1, len(l)):
        if i == j : 
            if i in d :
                d[i].append("me")
            else :
                d[i] = ["me"]
            continue
        if i in d :
            d[i].append((l[i] - l[j]) / (i - j))
        else :
            d[i] = [(l[i] - l[j]) / (i - j)]

c = [[0, 0, 0] for _ in range(N)]
for index, i in enumerate(d.values()) :
    # 자신보다 왼쪽
    h = 99999999999999
    temp = 0
    for j in range(index - 1, -1, -1) :
        if h > i[j] :
            h = i[j]
            temp += 1
    c[index][0] = temp

    # 자신보다 오른쪽
    h = -99999999999999
    temp = 0
    for j in range(index + 1, len(i)) :
        if h < i[j] :
            h = i[j]
            temp += 1
    c[index][1] = temp

    c[index][2] = c[index][0] + c[index][1]

c.sort(key = lambda x : -x[2])
print(c[0][-1])