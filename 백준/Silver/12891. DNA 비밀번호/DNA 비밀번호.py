from collections import deque

S, P = map(int, input().split())
DNA = input().rstrip()
l = list(map(int, input().split()))
d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

queue = deque()
for i in range(P):
    queue.append(DNA[i])
    if DNA[i] in d:
        l[d[DNA[i]]] -= 1

# print(queue)
# print(l)

def check(li):
    for i in li:
        if i > 0:
            return False
    return True

answer = 0
if check(l):
    answer += 1

for i in range(P, S):
    p = queue.popleft()
    queue.append(DNA[i])

    l[d[p]] += 1
    l[d[DNA[i]]] -= 1

    # print(queue)
    # print(l)

    if check(l):
        answer += 1

print(answer)
