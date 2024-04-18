#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    l = [[0] * N for _ in range(N)]
    cnt = N * N
    num = 1
    i, j = 0, 0

    while True :
        if num > N * N :
            break

        while j < N and l[i][j] == 0 :
            l[i][j] = num
            num += 1
            j += 1
            cnt -= 1

        i += 1
        j -= 1

        while i < N and l[i][j] == 0 :
            l[i][j] = num
            num += 1
            i += 1
            cnt -= 1
        
        i -= 1
        j -= 1
        
        while j >= 0 and l[i][j] == 0 :
            l[i][j] = num
            num += 1
            j -= 1
            cnt -= 1
        
        i -= 1
        j += 1

        while i >= 0 and l[i][j] == 0 :
            l[i][j] = num
            num += 1
            i -= 1
            cnt -= 1
        
        i += 1
        j += 1

    print(f'#{tc}')
    for i in l :
        print(*i)