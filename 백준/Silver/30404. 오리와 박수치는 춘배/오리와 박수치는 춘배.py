n, k = map(int, input().split())
x = list(map(int, input().split()))

cnt = 0
time = 0

for i in range(len(x)) :
    if x[i] > time :
        time = x[i] + k
        cnt += 1

print(cnt)