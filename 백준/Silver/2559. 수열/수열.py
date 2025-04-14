N, K = map(int, input().split())
l = list(map(int, input().split()))

hap = sum(l[:K])
answer = hap

for i in range(N - K) :
    hap = hap - l[i] + l[i + K]
    if (answer < hap) :
        answer = hap

print(answer)