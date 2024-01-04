from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    string = input()
    string = string.replace("RR", "")
    string = list(string)
    string.pop()
    len_list = int(input())
    l = input()
    l = l.replace("[", "")
    l = l.replace("]", "")
    l = l.replace(",", " ")
    l = deque(l.split())

    err = False
    r_count = 0
    for i in string :
        if i == 'R' :
            r_count += 1
        elif i == 'D' :
            if len(l) > 0 :
                if r_count % 2 != 0 :
                    l.pop()
                else :
                    l.popleft()
            else :
                err = True
                break
    if not err :
        l = list(map(int, l))
        if r_count % 2 != 0 :
            l.reverse()
        print("[", end = "")
        for i in range(len(l)) :
            if i == len(l) - 1 :
                print(l[i], end = "")
            else:
                print(l[i], end = ",")
        print("]")
    else :
        print("error")