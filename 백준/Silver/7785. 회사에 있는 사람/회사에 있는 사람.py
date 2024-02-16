import sys
input = sys.stdin.readline
n = int(input())
s = set()

for _ in range(n) :
    a, b = input().rstrip().split()
    if b == 'enter' :
        s.add(a)
    else :
        s.discard(a)

l = list(s)
l.sort(reverse = True)
for i in l :
    print(i)