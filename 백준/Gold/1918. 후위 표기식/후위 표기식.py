S = input().rstrip()
answer = []
stack = []

d = {'+': 1, '-': 1, '*': 2, '/': 2}

for i in range(len(S)):
    if S[i].isalpha():
        answer.append(S[i])
    elif S[i] == '(':
        stack.append(S[i])
    elif S[i] == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    elif S[i] in d:
        while stack and stack[-1] in d and d[stack[-1]] >= d[S[i]]:
            answer.append(stack.pop())
        stack.append(S[i])

while stack:
    answer.append(stack.pop())

print(''.join(answer))