import math

N = int(input())
l = list(map(int, input().split()))
a = l[0]

for i in range(1, len(l)):
    gcd = math.gcd(a, l[i])
    print(a // gcd, end="/")
    print(l[i] // gcd)
