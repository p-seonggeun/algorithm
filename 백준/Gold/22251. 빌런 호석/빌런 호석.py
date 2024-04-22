number = [
    # [1, 1, 1, 0, 1, 1, 1], # 0
    # [0, 0, 1, 0, 0, 1, 0], # 1
    # [1, 0, 1, 1, 1, 0, 1],
    # [1, 0, 1, 1, 0, 1, 1],
    # [0, 1, 1, 1, 0, 1, 0],
    # [1, 1, 0, 1, 0, 1, 1],
    # [1, 1, 0, 1, 1, 1, 1],
    # [1, 0, 1, 0, 0, 1, 0],
    # [1, 1, 1, 1, 1, 1, 1],
    # [1, 1, 1, 1, 0, 1, 1]
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2], # 0
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], # 4
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], # 7
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0] # 9
]

# diff = [[] for _ in range(10)]

# for i in range(10) :
#     for j in range(10) :
#         print(i, j)
#         temp = 0
#         if i == j :
#             diff[i].append(temp)
#             continue
#         for k in range(7) :
#             if number[i][k] != number[j][k] :
#                 temp += 1
#         diff[i].append(temp)

# for i in diff :
#     print(i)

N, K, P, X = map(int, input().split())
answer = 0
standard = '0' * (K - len(str(X))) + str(X)

for i in range(1, N + 1) :
    temp = '0' * (K - len(str(i))) + str(i)
    if temp == standard :
        continue
    # print(temp)
    a = 0
    for j in range(len(temp)) :
        if temp[j] == standard[j] :
            continue
        # print(temp[j], standard[j], number[int(standard[j])][int(temp[j])])
        a += number[int(standard[j])][int(temp[j])]
    if a <= P :
        answer += 1

print(answer)