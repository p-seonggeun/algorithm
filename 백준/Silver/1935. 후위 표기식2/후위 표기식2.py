N = int(input())
S = input().rstrip()
d = {}
stack = []

for i in range(N):
    d[chr(65 + i)] = int(input())

for i in range(len(S)):
    if S[i].isalpha():
        stack.append(S[i])

    else:
        b = stack.pop()
        a = stack.pop()
        if b in d:
            b = d[b]
        if a in d:
            a = d[a]
        result = eval(str(a) + S[i] + str(b))

        stack.append(result)

answer = stack.pop()
print("%.2f" % answer)