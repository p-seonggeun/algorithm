N = int(input())
l = []

for _ in range(N):
    l.append(int(input()))

def c(l):
    s = l[0]

    result = 1
    for i in l:
        if i > s:
            result += 1
            s = i

    return result

print(c(l))
print(c(l[::-1]))