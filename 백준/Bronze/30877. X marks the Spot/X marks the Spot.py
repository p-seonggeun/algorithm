import sys
input = sys.stdin.readline

N = int(input())
answer = ""
for _ in range(N):
    S, T = input().split()
    answer += T[S.upper().index('X')].upper()

print(answer)