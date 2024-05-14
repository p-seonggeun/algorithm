#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    l = list(map(int, input().split()))
    answer = 0
    m = 0
    for i in range(len(l) - 1, -1, -1) :
        if i == len(l) - 1 :
            m = l[i]
            continue
        else :
            if m >= l[i] :
                answer += m - l[i]
            else :
                m = l[i]

    print(f"#{tc}", answer)
