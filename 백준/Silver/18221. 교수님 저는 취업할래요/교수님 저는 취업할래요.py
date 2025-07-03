import math
N = int(input())
board = []
A = [0, 0]
B = [0, 0]
for i in range(N):
    temp = list(map(int, input().split()))
    if 2 in set(temp):
        A = [i, temp.index(2)]
    if 5 in set(temp):
        B = [i, temp.index(5)]
    board.append(temp)

def check1():
    if math.sqrt(abs(A[0] - B[0]) ** 2 + abs(A[1] - B[1]) ** 2) >= 5:
        return True
    return False

def check2():
    rs = min(A[0], B[0])
    re = max(A[0], B[0])
    cs = min(A[1], B[1])
    ce = max(A[1], B[1])

    t = 0
    for i in range(rs, re + 1):
        for j in range(cs, ce + 1):
            if board[i][j] == 1:
                t += 1

    if t >= 3:
        return True
    return False

def check3():
    t = 0
    rs = min(A[0], B[0])
    re = max(A[0], B[0])
    cs = min(A[1], B[1])
    ce = max(A[1], B[1])
    if A[0] == B[0]:
        for i in range(cs, ce + 1):
            if board[A[0]][i] == 1:
                t += 1
        if t >= 3:
            return True
        return False
    elif A[1] == B[1]:
        for i in range(rs, re + 1):
            if board[i][A[1]] == 1:
                t += 1
        if t >= 3:
            return True
        return False
    else:
        return True

if check1() and check2() and check3():
    print(1)
else:
    print(0)
