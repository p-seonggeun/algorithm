N, A, B = map(int, input().split())

C = N + (B - N)

if A < C:
    print("Bus")
elif A > C:
    print("Subway")
else:
    print("Anything")