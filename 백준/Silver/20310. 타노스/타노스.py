S = list(input().rstrip())

d = {}
for i in S :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

for i in d :
    d[i] = d[i] // 2

if '1' in d :
    i = 0
    while d['1'] > 0 :
        if S[i] == '1' :
            S[i] = '3'
            d['1'] -= 1
        i += 1

if '0' in d :
    i = len(S) - 1
    while d['0'] > 0 :
        if S[i] == '0' :
            S[i] = '3'
            d['0'] -= 1
        i -= 1

answer = ''
for i in S :
    if i != '3' :
        answer += i
print(answer)