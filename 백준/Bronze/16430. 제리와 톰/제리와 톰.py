import math
A, B = map(int, input().split())

P = B - A
g = math.gcd(B, P)
print(P // g, B // g)