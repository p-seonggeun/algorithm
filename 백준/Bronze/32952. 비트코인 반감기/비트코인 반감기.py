R, K, M = map(int, input().split())

a = M // K

while R > 0 and a > 0:
    R = R / 2
    a -= 1

print(int(R))