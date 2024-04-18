N = int(input())
M = int(input())
S = input().rstrip()

oi = 'I' + ('OI' * N)
ioi = 0
answer = 0
i = 0
while i < len(S) - 2 :
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I' :
        ioi += 1
        if ioi == N :
            answer += 1
            ioi -= 1
        i += 1
    else :
        ioi = 0
    i += 1

print(answer)