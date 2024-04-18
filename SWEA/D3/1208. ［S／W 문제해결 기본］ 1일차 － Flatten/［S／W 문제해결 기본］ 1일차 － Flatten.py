#import sys
#sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1) :
    dump = int(input())
    l = list(map(int, input().split()))
    for _ in range(dump) :
        l.sort()
        l[0] += 1
        l[-1] -= 1

        if max(l) - min(l) <= 1 :
            break

    print(f"#{tc}", max(l) - min(l))