import math
T = int(input())
for _ in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))

    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    else :
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if r1 + r2 == d or abs(r1 - r2) == d:
            print(1)
        elif r1 + r2 > d > abs(r1 - r2):
            print(2)
        else :
            print(0)