N = int(input())

for _ in range(N):
    s1, s2 = map(str, input().split())
    if (sorted(list(s1)) == sorted(list(s2))) :
        print('Possible')
    else :
        print('Impossible')