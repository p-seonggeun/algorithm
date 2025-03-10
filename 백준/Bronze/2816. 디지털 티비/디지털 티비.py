N = int(input())
l = []

for _ in range(N) :
    l.append(input().rstrip())

answer = ''
for i in range(0, N) :
    if l[i] == 'KBS1' :
        answer += '1' * i + '4' * i
        l.pop(i)
        break

for i in range(0, N - 1) :
    if l[i] == 'KBS2' :
        answer += '1' * (i + 1) + '4' * i
        break

print(answer)