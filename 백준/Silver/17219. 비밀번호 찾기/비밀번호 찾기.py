import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dict = {}
for _ in range(n) :
    site, pw = input().rstrip().split(" ")
    dict[site] = pw

for _ in range(m) :
    site = input().rstrip()
    print(dict[site])