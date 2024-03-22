n = int(input())
answer = 0
v1 = [0] * n
v2 = [0] * (2 * n - 1)
v3 = [0] * (2 * n - 1)

def queen(row) :
    global answer
    if row == n :
        answer += 1
        return
    
    for col in range(n) :
        if v1[col] == 0 and v2[row + col] == 0 and v3[row - col] == 0 :
            v1[col] = 1
            v2[row + col] = 1
            v3[row - col] = 1
            queen(row + 1)
            v1[col] = 0
            v2[row + col] = 0
            v3[row - col] = 0

queen(0)
print(answer)