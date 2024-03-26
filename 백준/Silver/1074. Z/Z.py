import sys
input = sys.stdin.readline

def dfs(n, r, c, q) :
    if n == 0 :
        return q
    
    half = 2 ** (n - 1)
    if r < half :
        if c < half :
            quad = 1
        else :
            quad = 2
            c -= half
    else :
        if c < half :
            quad = 3
            r -= half
        else :
            quad = 4
            r -= half
            c -= half
    q += (half ** 2) * (quad - 1)
    return dfs(n - 1, r, c, q)

N, r, c = map(int, input().split())
print(dfs(N, r, c, 0))