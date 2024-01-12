n, m = map(int, input().split())
d = []
b = []
for _ in range(n) :
    d.append(input())

for _ in range(m) :
    b.append(input())

result = {}

for i in d :
    if i in result :
        result[i] += 1
    else :
        result[i] = 1

for i in b :
    if i in result :
        result[i] += 1
    else :
        result[i] = 1

answer = []
for x, y in result.items() :
    if y == 2 :
        answer.append(x)

answer.sort()
print(len(answer))
for i in answer :
    print(i)