N, M = map(int, input().split())
num = list(map(int, input().split()))
money = []
for _ in range(N):
    money.append(list(map(int, input().split())))

answer = 0
for i in range(len(num) - 1):
    S, E = num[i], num[i + 1]
    answer += money[S - 1][E - 1]
print(answer)