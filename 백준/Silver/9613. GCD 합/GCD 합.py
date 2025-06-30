import math

t = int(input())

for _ in range(t):
    l = list(map(int, input().split()))
    n = l.pop(0)

    answer = 0
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if i != j:
                answer += math.gcd(l[i], l[j])
    print(answer)