N = input().rstrip()

s = ''
for i in range(int(N) + 1):
    s += str(i)

print(s.find(N))

