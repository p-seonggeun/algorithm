N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort()
print(l[K - 1])