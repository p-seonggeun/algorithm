import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    d = {}
    for _ in range(N) :
        a, b = map(str, input().rstrip().split())
        if b in d :
            d[b].append(a)
        else :
            d[b] = [a]
    answer = 1
    for i, j in d.items() :
        answer *= (len(j) + 1)
    
    print(answer - 1)