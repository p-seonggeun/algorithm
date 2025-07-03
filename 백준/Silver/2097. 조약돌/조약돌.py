N = int(input())

if N <= 4:
    print(4)
    exit(0)

c = 1
while True:
    if c ** 2 >= N:
        break
    c += 1

r = 1
while True:
    if r * c >= N:
        break
    r += 1

print(2 * ((r - 1) + (c - 1)))