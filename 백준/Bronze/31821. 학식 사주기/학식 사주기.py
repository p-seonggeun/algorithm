N = int(input())
menu = []
for _ in range(N):
    menu.append(int(input()))

M = int(input())
answer = 0
for _ in range(M):
    answer += menu[int(input()) - 1]
print(answer)