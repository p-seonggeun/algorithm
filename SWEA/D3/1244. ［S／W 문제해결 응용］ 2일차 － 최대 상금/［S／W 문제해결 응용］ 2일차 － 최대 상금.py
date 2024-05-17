#import sys
#sys.stdin = open("input.txt", "r")

def dfs(n) :
    global answer
    if n == B :
        answer = max(answer, int("".join(map(str, l))))
        return

    for i in range(length - 1) :
        for j in range(i + 1, length) :
            l[i], l[j] = l[j], l[i]

            key = int("".join(map(str, l)))
            if (n, key) not in v :
                dfs(n + 1)
                v.append((n, key))
            l[i], l[j] = l[j], l[i]

T = int(input())

for tc in range(1, T + 1) :
    A, B = map(int, input().split())
    l = [int(i) for i in str(A)]
    length = len(l)
    answer = 0
    v = []
    dfs(0)
    print(f"#{tc}", answer)