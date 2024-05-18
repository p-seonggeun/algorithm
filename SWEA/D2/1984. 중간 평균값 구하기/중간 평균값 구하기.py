#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T + 1) :
    answer = 0
    l = sorted(list(map(int, input().split())))
    answer = int(round(sum(l[1:9]) / 8, 0))


    print(f"#{tc}", answer)