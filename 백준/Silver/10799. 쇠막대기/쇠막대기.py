import sys
input = sys.stdin.readline

s = input().rstrip()

answer = 0
stack = []

for index, i in enumerate(s) :
    if i == '(' :
        stack.append(index)
    elif i == ')' :
        if index - stack[-1] == 1 :
            stack.pop()
            answer += len(stack)
        else :
            stack.pop()
            answer += 1
            
print(answer)