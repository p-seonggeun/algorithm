N, K = map(int, input().split())

stage = 1
while stage != N:
    K = K // 2
    stage += 1
print(K)
