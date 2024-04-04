import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = []
temp = set()
answer = 0
for _ in range(N) :
    belt.append(int(input()))

for i in range(k) :
    belt.append(belt[i])

for i in range(N) :
    temp = set(belt[i : (i + k)])
    temp.add(c)
    answer = max(answer, len(temp))

print(answer)