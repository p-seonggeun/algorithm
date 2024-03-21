import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def cantorian(n, s) :
    if n == 0 :
        return s
    else :
        d = int((3 ** n) * (1 / 3))
        left = s[:d]
        right = s[2*d:]
        return cantorian(n - 1, left) + " " * d + cantorian(n - 1, right)

while True :
    n = input().rstrip()
    if n == '' :
        break
    n = int(n)
    s = '-' * (3 ** n)
    print(cantorian(n, s))