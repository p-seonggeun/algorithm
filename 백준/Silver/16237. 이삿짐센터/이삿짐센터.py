A,B,C,D,E=map(int,input().split())
answer=0
answer+=E

while D>0:
    if A>0:
        A-=1
    D-=1
    answer+=1

while C>0:
    if B>0:
        B-=1
    elif A>0:
        A-=2
    C-=1
    answer+=1

while B>0:
    if B>=2 and A>=1:
        B-=2
        A-=1
    elif B>=1 and A>=1:
        B-=1
        A-=3
    else:
        B-=2
    answer+=1

while A>0:
    A-=5
    answer+=1

print(answer)