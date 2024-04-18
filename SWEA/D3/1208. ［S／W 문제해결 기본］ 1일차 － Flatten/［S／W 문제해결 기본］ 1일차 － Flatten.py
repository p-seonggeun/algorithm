#import sys
#sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1) :
    dump = int(input())
    l = list(map(int, input().split()))

    while dump > 0 :
        dump -= 1
        a = l.index(min(l))
        b = l.index(max(l))
        l[a] += 1
        l[b] -= 1
    
    print(f"#{tc}", max(l) - min(l))