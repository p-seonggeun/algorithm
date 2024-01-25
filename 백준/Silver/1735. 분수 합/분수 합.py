import math

a_bj, a_bm = map(int, input().split())
b_bj, b_bm = map(int, input().split())

r_bj = (a_bj * b_bm) + (b_bj * a_bm)
r_bm = a_bm * b_bm

gcd = math.gcd(r_bj, r_bm)

if gcd == 1 :
    print(r_bj, r_bm)
else :
    r_bj = r_bj // gcd
    r_bm = r_bm // gcd
    print(r_bj, r_bm)