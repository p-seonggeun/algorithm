N = int(input())
answer = 0
for i in range(N):
    a, b = map(int, input().split())

    temp = answer % (a + b)
    if temp < b:
        answer += b - temp

    answer += 1
print(answer)