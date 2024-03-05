import sys
import math
input = sys.stdin.readline

n = int(input())
tree = set()

for _ in range(n) :
    tree.add(int(input()))

tree_l = list(tree)
tree_l.sort()
g = 0
for i in range(len(tree_l) - 1) :
    if i == 0 :
        g = abs(tree_l[i] - tree_l[i + 1])
        continue
    g = math.gcd(g, tree_l[i] - tree_l[i + 1])

answer = ((tree_l[-1] - tree_l[0]) // g) + 1 - n
print(answer)
