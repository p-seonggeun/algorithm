n = input()
l = []
for i in range(0, len(n), 10) :
    l.append(n[i : i + 10])

for i in l :
    print(i)