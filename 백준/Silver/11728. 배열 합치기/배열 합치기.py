N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = A + B
l.sort()
print(" ".join(map(str, l)))