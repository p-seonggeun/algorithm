import sys
input = sys.stdin.readline

n = int(input())
emogi = set()
answer = 0 
for _ in range(n) :
    log = input().rstrip()
    if log == "ENTER" :
        emogi = set()
    else :
        if log not in emogi :
            emogi.add(log)
            answer += 1

print(answer)