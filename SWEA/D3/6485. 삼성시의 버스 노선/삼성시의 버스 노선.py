#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    cnt = [0] * 5001
    answer = []
    for _ in range(N) :
        a, b = map(int, input().split())
        for i in range(a, b + 1) :
            cnt[i] += 1
    P = int(input())
    for _ in range(P) :
        answer.append(cnt[int(input())])
    
    print(f'#{tc}', *answer)