import sys
input = sys.stdin.readline
s = input().rstrip()
b = input().rstrip()
stack = []

for i in s :
    stack.append(i)
    if len(stack) >= len(b) :
        if ''.join(stack[len(stack) - len(b):]) == b :
            del stack[len(stack) - len(b):]

if stack :
    print(''.join(stack))
else :
    print("FRULA")