# 문자열 길이가 같은 경우

# 문자열 길이가 다른 경우
# 앞에서 추가하는 경우, 뒤에서 추가하는 경우 dfs
# 종료조건은 문자열 길이가 같아지는 경우
# 앞에서부터 A의 문자열이 T인지, 아니면 A랑 B랑 같은지
from collections import deque

answer = 1e9
temp = 0
A, B = input().split()
def dfs(s) :
    global answer
    global temp
    if len(s) == len(B) :
        for i in range(len(s)) :
            if s[i] == 'T' or s[i] == B[i] :
                temp += 1
        answer = min(answer, len(B) - temp)
        temp = 0
        return

    s.append('T')
    dfs(s)
    s.pop()

    s.appendleft('T')
    dfs(s)

queue = deque()
for i in A :
    queue.append(i)
dfs(queue)
print(answer)