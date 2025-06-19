l = []
for i in range(1, 9) :
    l.append((i, int(input())))

l.sort(key = lambda x : -x[1])
answer = []
score = []
for i in l :
    if len(answer) == 5 :
        break
    answer.append(i[0])
    score.append(i[1])

answer.sort()
print(sum(score))
print(*answer)