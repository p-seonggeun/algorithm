import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n) :
    t = input().rstrip()
    stack = []
    for i in t :
        if stack :
            if i == 'A' and stack[-1] == i :
                stack.pop()
            elif i == 'B' and stack[-1] == i :
                stack.pop()
            else :
                stack.append(i)
        else :
            stack.append(i)
    if not stack :
        answer += 1
print(answer)