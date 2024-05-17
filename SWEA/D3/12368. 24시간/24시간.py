#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    A, B = map(int, input().split())
    answer = 0
    if A + B > 24 :
        answer = A + B - 24
    elif A + B == 24 :
        answer = 0
    else :
        answer = A + B

    print(f"#{tc}", answer)