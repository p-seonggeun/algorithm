A, B = map(int, input().split())

if A > B :
    l = [i for i in range(B + 1, A)]
    print(len(l))
    print(' '.join(map(str, l)))
if A < B :
    l = [i for i in range(A + 1, B)]
    print(len(l))
    print(' '.join(map(str, l)))
if A == B :
    print(0)