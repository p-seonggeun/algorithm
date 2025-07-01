from itertools import permutations
N = int(input())
l = [i + 1 for i in range(N)]
for i in permutations(l):
    print(*i)