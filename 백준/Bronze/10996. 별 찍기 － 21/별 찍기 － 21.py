N = int(input())

for i in range(N): # 전체
    for j in range(N):
        if j % 2 != 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()

    for j in range(N):
        if j % 2 == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()