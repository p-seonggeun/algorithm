l = list(input())
n = 0
while l :
    n += 1
    for i in str(n) :
        if not l :
            break
        if l[0] == i :
            l.pop(0)

print(n)