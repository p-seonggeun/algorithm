import sys
input = sys.stdin.readline

n = int(input())
dance = set()
for _ in range(n) :
    a, b = input().rstrip().split(" ")
    if a == 'ChongChong' or b == 'ChongChong' :
        dance.add(a)
        dance.add(b)
    else :
        if 'ChongChong' in dance :
            if a in dance or b in dance :
                dance.add(a)
                dance.add(b)

print(len(dance))