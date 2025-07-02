import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    m = int(input())
    l = []
    for _ in range(m):
        l.append(input().rstrip())
    n = int(input())

    t = []
    for _ in range(n):
        p = list(map(int, input().split()))
        k = p.pop(0)
        temp = ""
        for j in p:
            temp += l[j]
        t.append(temp)
    print(f"Scenario #{i + 1}:")
    for j in t:
        print(j)

    print()