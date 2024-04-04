import sys
input = sys.stdin.readline
P = int(input())

for _ in range(P) :
    answer = 0
    temp = list(map(int, input().split(" ")))
    index = temp.pop(0)
    stack = []
    while temp :
        height = temp.pop(0)
        if not stack :
            stack.append(height)
        else :
            if stack[-1] < height :
                stack.append(height)
            else :
                for i in range(len(stack)) :
                    if stack[i] > height :
                        answer += len(stack) - i
                        stack.insert(i, height)
                        break
    print(index, answer)