import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n) :
    name, kor, eng, math = input().rstrip().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    temp = [name, kor, eng, math]
    l.append(temp)

l = sorted(l, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in l :
    print(i[0])