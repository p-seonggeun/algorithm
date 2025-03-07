import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    s = input().rstrip()
    l = []
    temp = []
    for i in s :
        if i == '<' :
            if l :
                temp.append(l.pop())
        elif i == '>' :
            if temp :
                l.append(temp.pop())
        elif i == '-' :
            if l :
                l.pop()
        else :
            l.append(i)
    
    while temp :
        l.append(temp.pop())
        
    print(''.join(l))