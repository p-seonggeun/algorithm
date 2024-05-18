#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())

for tc in range(1, T + 1) :
    l = list(input().rstrip())
    for i in range(10, -1, -1) :
        if (l[0 : i + 1] == l[i + 1 : i + i + 1 + 1]) :
            answer = l[0 : i + 1]

    print(f"#{tc}", len(''.join(answer)))