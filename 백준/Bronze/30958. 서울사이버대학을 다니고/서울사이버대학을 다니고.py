N = int(input())
l = list(input().replace(" ", ""))
d = {}
for i in l:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

print(max(d.values()))