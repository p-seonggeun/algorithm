import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    l = [int(input()) for i in range(n)]
    if sum(l) == 0:
        print("0")
    elif sum(l) > 0:
        print("+")
    else:
        print("-")