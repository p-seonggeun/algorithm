import sys
input = sys.stdin.readline

def dfs(n, cnt) :
    global answer
    # 가지 치기(끝까지 진행해도 정답 갱신이 불가능 한 경우)
    if answer >= (cnt + (N - n) * 2) :
        return
    if n == N : # 종료 조건
        answer = max(answer, cnt)
        return
    
    if S[n] <= 0 : # 내 계란이 깨진 경우 -> 다음 계란으로
        dfs(n + 1, cnt)
    else : # 내 계란이 안 깨진 상태
        # 하부 함수 호출
        flag = False
        for j in range(N) : 
            if n == j or S[j] <= 0 :
                continue
            flag = True
            # 계란 부딪히기
            S[n] -= W[j]
            S[j] -= W[n]
            dfs(n + 1, cnt + int(S[n] <= 0) + int(S[j] <= 0))
            S[n] += W[j]
            S[j] += W[n]
        if flag == False : # 한번도 안부딪혔다면
            dfs(n + 1, cnt)

N = int(input())
S = []
W = []
for _ in range(N) :
    s, w = map(int, input().split())
    S.append(s)
    W.append(w)
answer = 0
dfs(0, 0)
print(answer)