import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N) :
    l.append(int(input()))

l.sort(reverse = True)

answer = 0
temp = []
for i in l :
    temp.append(i)
    kg = temp[-1] * len(temp)
    if kg > answer :
        answer = kg

print(answer)
