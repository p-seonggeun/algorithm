for _ in range(3) :
    l = list(map(int, input().split()))
    if l.count(1) == 0 :
        print('D')
        continue
    if l.count(1) == 1 :
        print('C')
        continue
    if l.count(1) == 2 :
        print('B')
        continue
    if l.count(1) == 3 :
        print('A')
        continue
    if l.count(1) == 4 :
        print('E')
        continue