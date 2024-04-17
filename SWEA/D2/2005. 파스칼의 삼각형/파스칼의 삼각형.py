#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    l = [[1] * (i + 1) for i in range(N)]

    for index, i in enumerate(l) :
        for j in range(len(i) - 1) :
            if j == 0 :
                l[index][j] = l[index - 1][j]
            else :
                l[index][j] = l[index - 1][j - 1] + l[index - 1][j]
    print(f'#{tc}')
    for i in l :
        print(*i)