#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1) :
    N, Q = map(int, input().split())
    answer = [0] * N
    for q in range(1, Q + 1) :
        L, R = map(int, input().split())
        for j in range(L - 1, R) :
            answer[j] = q
    print("#", end = "")
    print(tc, *answer)