S = input().rstrip()
l = []

for i in range(len(S)) :
    l.append(S[i:])

l.sort()
for i in l :
    print(i)