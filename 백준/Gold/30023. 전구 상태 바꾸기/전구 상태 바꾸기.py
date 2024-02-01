INF = 999999
n = int(input())
l = list(input())
count = 0
light = {'R' : 'G', 'G' : 'B', 'B' : 'R'}
light_int = {0 : 'R', 1 : 'G', 2 : 'B'}
target = ''
answer = INF
for i in range(3) :
    temp = l.copy()
    target = light_int[i]
    count = 0
    for j in range(n - 2) :
        if temp[j] == target : # 타겟과 일치할때
            continue
        else : # 타겟과 불일치할때
            # 돌리는 횟수를 정해야함
            while target != temp[j] :
                if target == temp[j] :
                    break
                else :
                    temp[j], temp[j + 1], temp[j + 2] = light[temp[j]], light[temp[j + 1]], light[temp[j + 2]]
                    count += 1

    if temp.count(target) == n :
        if answer > count :
            answer = count

if answer != INF :
    print(answer)
else :
    print(-1)