n = int(input())
l = [64]

while sum(l) != n :
    if sum(l) > n :
        mini = min(l)
        temp = mini // 2
        l.pop()
        l.append(temp)
        if sum(l) < n :
            l.append(temp)

print(len(l))