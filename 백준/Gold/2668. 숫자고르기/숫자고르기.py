import sys
input = sys.stdin.readline
N = int(input())
l1 = [i + 1 for i in range(N)]
l2 = []

for _ in range(N) :
    l2.append(int(input()))

answer = []

def dfs(index, count) :
    if count > N :
        return
    
    if A and B and A == B :
        answer.extend(list(A))
        return
    
    A.add(l1[index])
    B.add(l2[index])
    dfs(l2[index] - 1, count + 1)

for i in range(N) :
    A, B = set(), set()
    dfs(i, 0)

answer = set(answer)
print(len(answer))
for i in sorted(answer) :
    print(i)