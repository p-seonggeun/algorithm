import math
X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

R = math.sqrt(abs(X2 - X1) ** 2 + abs(Y2 - Y1) ** 2)
if R >= R1 + R2:
    print("NO")
else:
    print("YES")