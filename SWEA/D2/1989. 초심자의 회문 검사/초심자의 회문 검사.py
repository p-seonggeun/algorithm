#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T + 1) :
    answer = 0
    s = input().rstrip()
    if s == s[::-1] :
        answer = 1

    print(f"#{tc}", answer)