import sys
input = sys.stdin.readline

N = int(input())
stack = []

answer = 0
for _ in range(N) :
    h = int(input())

    if stack :
        while (stack and stack[-1] <= h) :
            stack.pop()
        answer += len(stack)
        stack.append(h)
    else :
        stack.append(h)

print(answer)