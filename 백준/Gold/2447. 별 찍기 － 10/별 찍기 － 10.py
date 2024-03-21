n = int(input())
def star(n) :
    if n == 1 :
        return ['*']
    
    else :
        index = n // 3
        stars = star(index)

        l = []

        for i in stars :
            l.append(i * 3)
        for i in stars :
            l.append(i + ' ' * index + i)
        for i in stars :
            l.append(i * 3)
        
        return l
    
for i in star(n) :
    print(i)