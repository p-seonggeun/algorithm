T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    l = list(map(int, input().split()))
    answer = 0

    for i in l:
        answer += i // K
    print(answer)