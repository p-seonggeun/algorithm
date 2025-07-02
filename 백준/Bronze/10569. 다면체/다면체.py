T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    answer = 2 - V + E
    print(answer)