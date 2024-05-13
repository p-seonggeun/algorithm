#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    fish = 0
    time = 0
    flag = True

    while time <= 11113 :
        if time in people :
            if time != 0 and time % M == 0:
                fish += K
            fish -= 1
            if fish < 0 :
                flag = False
                break
        else :
            if time != 0 and time % M == 0:
                fish += K
        time += 1

    if flag :
        print(f"#{tc} Possible")
    else :
        print(f"#{tc} Impossible")