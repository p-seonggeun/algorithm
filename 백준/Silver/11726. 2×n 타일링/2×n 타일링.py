n = int(input())
d = [0] * 1001

def dp(x) :
    if x == 1 :
        return 1
    elif x == 2 :
        return 2
    elif d[x] != 0 :
        return d[x]
    else :
        d[x] = (dp(x - 1) + dp(x - 2)) % 10007
        return d[x]

print(dp(n))