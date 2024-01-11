import sys
sys.setrecursionlimit(10000)

n = int(input())
d = [0] * 1001

def dp(x) :
    if x == 1 :
        return 1
    elif x == 2 :
        return 3
    elif d[x] != 0 :
        return d[x]
    else :
        d[x] = (dp(x - 1) + 2 * dp(x - 2)) % 10007
        return d[x]

print(dp(n))