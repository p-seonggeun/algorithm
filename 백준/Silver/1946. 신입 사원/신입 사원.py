import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    l = []
    temp = []
    count = 1

    for _ in range(n) :
        l.append(list(map(int, input().rstrip().split())))

    l.sort()
    
    first = l[0][0]
    second = l[0][1]

    for i in range(1, n) :
        if first < l[i][0] : # 1차점수 순위가 낮다면
            if second > l[i][1] : # 2차점수 순위가 높다면
                count += 1
                temp.append(l[i])
                first = l[i][0]
                second = l[i][1]

    print(count)