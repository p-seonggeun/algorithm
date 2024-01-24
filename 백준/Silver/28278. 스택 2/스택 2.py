import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n) :
    l = list(map(int, input().split()))
    if len(l) == 1 :
        if l[0] == 2 :
            if len(stack) != 0 :
                print(stack.pop())
            else :
                print(-1)
        elif l[0] == 3 :
            print(len(stack))
        elif l[0] == 4 :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif l[0] == 5 :
            if len(stack) != 0 :
                print(stack[-1])
            else :
                print(-1)
    else :
        stack.append(l[1])