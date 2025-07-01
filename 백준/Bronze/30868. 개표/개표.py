T = int(input())
for _ in range(T):
    n = int(input())

    p = n // 5
    m = n % 5

    for i in range(p):
        print("++++", end = " ")

    for i in range(m):
        print("|", end = "")
    print()