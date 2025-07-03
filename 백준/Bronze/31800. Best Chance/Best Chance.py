import sys
input = sys.stdin.readline
# 기회비용 = 자신을 제외한 나머지 물건의 이익 중 가장 큰 값 - 자신의 가격
# 순수익 = 이익 - 기회비용 - 가격

N = int(input())
e = list(map(int, input().split()))
E = sorted(e, reverse=True)
p = list(map(int, input().split()))
g = []


for i in range(len(e)):
    if e[i] == E[0]:
        g.append(E[1] - p[i])
    else:
        g.append(E[0] - p[i])

answer = []
for i in range(len(e)):
    temp = e[i] - g[i] - p[i]
    answer.append(temp)
print(*answer)