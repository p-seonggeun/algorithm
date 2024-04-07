from itertools import permutations
S = input().rstrip()
d = {}
for i in S :
    if i in d :
        d[i] += 1
    else :
        d[i] = 1

d['0'] = d['0'] // 2
d['1'] = d['1'] // 2

l = ['0'] * d['0'] + ['1'] * d['1']
l.sort()
print(''.join(l))