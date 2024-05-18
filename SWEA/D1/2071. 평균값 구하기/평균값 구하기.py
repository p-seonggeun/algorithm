#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    l = list(map(int, input().split()))
    answer = 0
    answer = int(round(sum(l) / len(l), 0))

    print(f"#{tc}", answer)