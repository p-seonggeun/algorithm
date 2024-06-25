N = int(input())
l = []

def sum_num(s) :
    h = 0
    for i in s :
        if i.isnumeric() :
            h += int(i)
    return h

for _ in range(N) :
    l.append(input().rstrip())

l.sort(key = lambda x : (len(x), sum_num(x), x))

for i in l :
    print(i)