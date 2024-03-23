import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
stack = []
answer = [-1] * n
for i in range(n) :
    while stack != [] and l[stack[-1]] < l[i] :
        answer[stack.pop()] = l[i]
    stack.append(i)

print(*answer)