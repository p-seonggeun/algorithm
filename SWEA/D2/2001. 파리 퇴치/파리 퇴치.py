#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    N, M = map(int, input().split())
    l = []
    for _ in range(N) :
        l.append(list(map(int, input().split())))
    answer = 0
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            temp = 0
            for a in range(i, i + M) :
                for b in range(j, j + M) :
                    temp += l[a][b]
            answer = max(answer, temp)
    print(f'#{tc}', answer)