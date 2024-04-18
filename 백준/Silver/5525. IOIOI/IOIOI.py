N = int(input())
M = int(input())
S = input().rstrip()

oi = 'I' + ('OI' * N)
answer = 0 
for i in range(len(S) - len(oi) + 1) :
    if S[i: i + len(oi)] == oi :
        answer += 1

print(answer)