#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    N = int(input())
    room = [0 for _ in range(200)]
    d = {}
    for i in range(1, 401) :
        if i in d :
            continue
        if i not in d :
            d[i] = i + 1
            d[i + 1] = i

    for _ in range(N) :
        s, e = map(int, input().split())
        if s > e :
            s, e = e, s
        if s == d[e] and d[s] == e : # 1칸 차이일 경우
            if s % 2 == 0 : # 짝수일때
                room[((s - 2) // 2)] += 1
            else :
                room[((s - 1) // 2)] += 1
        else :
            if s % 2 == 0 : s = (s - 2) // 2
            else : s = (s - 1) // 2
            if e % 2 == 0 : e = (e - 2) // 2
            else : e = (e - 1) // 2

            for i in range(s, e + 1) :
                room[i] += 1

    if max(room) == 0 :
        print(f"#{tc}", max(room))
    else:
        print(f"#{tc}", max(room))
