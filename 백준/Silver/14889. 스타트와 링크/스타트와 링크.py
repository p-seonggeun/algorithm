def calc(start, link) :
    s_s = 0
    l_s = 0
    for i in range(N // 2) :
        for j in range(N // 2) :
            if i == j :
                continue
            row = start[i]
            col = start[j]
            s_s += stat[row - 1][col - 1]
            row = link[i]
            col = link[j]
            l_s += stat[row - 1][col - 1]

    return abs(s_s - l_s)

def dfs(index, count) :
    global answer
    if count == N // 2 :
        l = standard - set(temp)
        if tuple(temp) not in stand and tuple(l) not in stand :
            stand.add(tuple(temp))
            stand.add(tuple(l))
            answer = min(answer, calc(temp, list(l)))
        return

    for i in range(index, N) :
        if not visited[i] :
            visited[i] = True
            temp.append(i + 1)
            dfs(i, count + 1)
            temp.pop()
            visited[i] = False

import sys
input = sys.stdin.readline
N = int(input())
stat = []
temp = []
stand = set()
answer = 99999999999
standard = set(i + 1 for i in range(N))
for _ in range(N) :
    stat.append(list(map(int, input().split())))
visited = [False for _ in range(N)]

dfs(0, 0)
print(answer)