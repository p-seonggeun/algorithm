import sys
input = sys.stdin.readline

n = int(input())
e = int(input())
answer = []
dictionary = {}
sing = 0

for _ in range(e) :
    l = list(map(int, input().split()))
    k = l.pop(0)

    if 1 in l :
        sing += 1
        for i in l :
            if i in dictionary :
                dictionary[i].add(sing)
            else :
                dictionary[i] = set([sing])
    else :
        u = set()

        for i in l :
            if i in dictionary :
                u = u.union(dictionary[i])
            else :
                dictionary[i] = set()

        for i in l :
            for j in list(u) :
                dictionary[i].add(j)

standard = dictionary[1]

for i in sorted(list(dictionary.keys())) :
    if standard == dictionary[i] :
        print(i)