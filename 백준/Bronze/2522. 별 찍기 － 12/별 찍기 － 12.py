N = int(input())
for i in range(N - 1, 0, -1):
    print(" " * i, end = "")
    print("*" * (N - i))

for i in range(N):
    print(" " * i, end = "")
    print("*" * (N - i))