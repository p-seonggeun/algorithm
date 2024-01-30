n = int(input())
l = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(n) :
    x, y = map(int, input().split())
    for i in range(10) :
        for j in range(10) :
            l[y + i][x + j] = 1

for i in l :
    result += i.count(1)

print(result)