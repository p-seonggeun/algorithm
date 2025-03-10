N = list(input())

temp = 0
for i in N :
    temp += int(i)

N.sort(reverse=True)
if '0' in N and temp % 3 == 0 :
    print(''.join(N))
else :
    print(-1)