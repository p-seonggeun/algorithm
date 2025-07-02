N, L = map(int, input().split())
answer = [0, 0]
for _ in range(N):
    black = input().replace("0", " ")
    temp = 0
    for i in black.split(" "):
        if i != '':
            temp += 1
    if temp > answer[0]:
        answer[0] = temp
        answer[1] = 1
    elif temp == answer[0]:
        answer[1] += 1
print(*answer)