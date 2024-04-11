import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    W = input().rstrip()
    K = int(input())
    d = {}
    three = 99999999
    four = -99999999
    flag = False
    for index, i in enumerate(W) :
        if i in d : d[i].append(index)
        else : d[i] = [index]
    
    for i, j in d.items() :
        if len(j) >= K :
            flag = True
            for k in range(len(j) - K + 1) :
                temp = abs(j[k] - j[k + K - 1]) + 1
                if three >= temp :
                    three = temp
                if four <= temp :
                    four = temp

    if not flag :
        print(-1)
    else :
        print(three, four)