#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T + 1) :
    l = list(map(int, input().split()))
    answer = 0
    for i in l :
        if i % 2 != 0 :
            answer += i

    print(f"#{tc}", answer)