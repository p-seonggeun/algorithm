answer = 0
for j in range(2):
    a, b = map(int, input().split())
    c = a + b
    for i in range(c):
        answer += 1
        if answer > 4:
            answer = 1
    if j == 0:
        answer -= 1
print(answer)