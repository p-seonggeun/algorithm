import sys
input = sys.stdin.readline

N = int(input())
s = set()
for i in range(N) :
    if i == 0 :
        answer = input().rstrip()
    else :
        temp = input().rstrip()
        for j in range(len(temp)) :
            if answer[j] != temp[j] :
                s.add(j)

a = ''
for i in range(len(answer)) :
    if i in s :
        a += '?'
    else : a += answer[i]

print(a)