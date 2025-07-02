import math

N = int(input())
l = list(map(int, input().split()))
T, P = map(int, input().split())

answer = 0
for i in l:
    answer += math.ceil(i / T)
print(answer)
print(N // P, N % P)