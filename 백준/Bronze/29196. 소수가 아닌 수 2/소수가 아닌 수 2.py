import math

k = input().rstrip()
p = k.split(".")[1]
q = 10 ** (len(p))
p = int(p)

g = math.gcd(p, q)

print("YES")
print(p // g, q // g)