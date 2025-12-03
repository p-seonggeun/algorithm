N, K = map(int, input().split())

answer = 0
for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            i = str(i)
            j = str(j)
            k = str(k)

            if len(i) == 1:
                i = '0' + i
            if len(j) == 1:
                j = '0' + j
            if len(k) == 1:
                k = '0' + k

            if str(K) in (i + j + k):
                answer += 1

print(answer)