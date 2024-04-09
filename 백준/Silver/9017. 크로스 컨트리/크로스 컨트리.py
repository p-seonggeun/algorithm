import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    score = list(map(int, input().split()))
    s = set(score)
    t = [] # 점수 제외 팀
    for i in s :
        if score.count(i) < 6 :
            t.append(i)
    l = []

    cnt = 0
    for index, i in enumerate(score) :
        if i in t :
            l.append(0)
        else :
            cnt += 1
            l.append(cnt)

    sd = {}
    for i, j in zip(score, l) :
        if j == 0 :
            continue
        if i in sd :
            sd[i].append(j)
        else :
            sd[i] = [j]
    
    answer = [0, 999999]
    for i in sd :
        if answer[1] > sum(sd[i][:4]) :
            answer = [i, sum(sd[i][:4])]
        elif answer[1] == sum(sd[i][:4]) :
            if sd[answer[0]][4] > sd[i][4] :
                answer = [i, sum(sd[i][:4])]
    print(answer[0])
