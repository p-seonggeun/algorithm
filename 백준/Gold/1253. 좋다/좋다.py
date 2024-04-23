import sys
input = sys.stdin.readline

N = int(input())
l = sorted(list(map(int, input().split())))
answer = 0

def check(ind, target) :
    if ind == 0 :
        start = 1
        end = N - 1
    elif ind == N - 1 :
        start = 0
        end = N - 2
    else :
        start = 0
        end = N - 1
    
    while start < end :
        if start == ind :
            start += 1
            continue
        elif end == ind :
            end -= 1
            continue

        if target == l[start] + l[end] :
            return True
        
        elif l[start] + l[end] > target :
            end -= 1

        elif l[start] + l[end] < target :
            start += 1
    return False

for index, i in enumerate(l) :
    if check(index, i) :
        answer += 1

print(answer)