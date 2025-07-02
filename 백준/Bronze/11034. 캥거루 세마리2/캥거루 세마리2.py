while True:
    try:
        A, B, C = map(int, input().split())
        temp1 = 0
        for i in range(A + 1, B):
            temp1 += 1

        temp2 = 0
        for i in range(B + 1, C):
            temp2 += 1
        print(max(temp1, temp2))
    except:
        exit()