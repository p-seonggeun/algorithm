import copy

n = int(input())
num = 1
l = list(map(int, input().split()))
standard = copy.deepcopy(l)
standard.sort()
temp = []
result = []

while len(result) != n :
    while l :
        a = l.pop(0)
        if num == a :
            result.append(a)
            num += 1
            if temp :
                while num == temp[-1] :
                    result.append(temp.pop())
                    num += 1
                    if not temp :
                        break
                
        else :
            if temp :
                if a > temp[-1] :
                    print("Sad")
                    exit(0)
            temp.append(a)

if result == standard :
    print("Nice")
else :
    print("Sad")