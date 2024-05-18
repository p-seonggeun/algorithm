#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    A, B = map(int, input().split())
    if A < B :
        answer = "<"
    elif A == B :
        answer = "="
    else :
        answer = ">"

    print(f"#{tc}", answer)