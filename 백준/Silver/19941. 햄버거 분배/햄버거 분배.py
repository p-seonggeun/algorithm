import sys
input = sys.stdin.readline
N, K = map(int, input().split())
table = list(input().rstrip())
answer = 0
for i in range(len(table)) :
    if table[i] == 'H' :
        table[i] = 0

for i in range(len(table)) :
    if table[i] == 'P' :
        s = i - K
        e = i + K
        if s < 0 : s = 0
        if e >= N : e = N - 1

        for j in range(s, e + 1) :
            if table[j] == 0 :
                table[j] += 1
                answer += 1
                break

print(answer)