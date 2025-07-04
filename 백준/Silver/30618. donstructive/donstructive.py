N = int(input())
l = [i + 1 for i in range(N)]
seq = []
start = 0
end = N - 1

while len(seq) != N:
    seq.append(start)
    start += 1

    if len(seq) == N:
        break

    seq.append(end)
    end -= 1

answer = [0 for _ in range(N)]
for index, i in enumerate(seq):
    answer[i] = index + 1

print(*answer)