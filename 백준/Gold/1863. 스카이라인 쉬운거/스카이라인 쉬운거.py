import sys
input = sys.stdin.readline
N = int(input())
stack = []
answer = 0

for _ in range(N) :
    x, y = map(int, input().split())
    if y == 0 :
        stack = []
        continue
    
    if not stack :
        stack.append(y)
        answer += 1
    else :
        if stack[-1] > y :
            while stack and stack[-1] > y :
                stack.pop()
            if y not in stack :
                stack.append(y)
                answer += 1
        else :
            if y not in stack :
                stack.append(y)
                answer += 1

print(answer)
