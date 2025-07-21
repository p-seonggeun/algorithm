def solution(beginning, target):
    answer = 0 
    row, col = len(target), len(target[0])
    board = [[0 for _ in range(col)] for _ in range(row)]
    def check1():
        count = 0
        for i in range(row):
            for j in range(col):
                if beginning[i][j] == target[i][j]:
                    board[i][j] = 1
        
        temp = []
        for i in board:
            temp.append(i[::])
        
        # 0행의 열들을 순차적으로 돌면서 열을 쭉 바꿈
        for i in range(col):
            if temp[0][i] == 0:
                count += 1
                for j in range(row):
                    if temp[j][i] == 0:
                        temp[j][i] = 1
                    else:
                        temp[j][i] = 0
        
        # 0열의 행들을 순차적으로 돌면서 행을 쭉 바꿈
        for i in range(row):
            if temp[i][0] == 0:
                count += 1
                for j in range(col):
                    if temp[i][j] == 0:
                        temp[i][j] = 1
                    else:
                        temp[i][j] = 0
        
        for i in range(row):
            for j in range(col):
                if temp[i][j] == 0:
                    return -1
        return count
        
    # --- 되는지 안되는지 확인 끝
    # 남은건 0,0이 1인 경우와 0인 경우

    def check2(): # 0,0 -> 1일때 안돌리는 경우
        count = 0
        for i in range(1, row): # 0열에서 행을 돌리면서 0인 것들 count
            if board[i][0] == 0:
                count += 1
        for i in range(1, col): # 0열에서 열을 돌리면서 0인 것들 count
            if board[0][i] == 0:
                count += 1
        
        print("check2 count:", count)
        return count
    
    def check3(): # 0,0 -> 1일때 행과 열 둘 다 돌리는 경우
        count = 0
        # 행을 돌면서 1인 것들 카운트
        for i in range(1, row):
            if board[i][0] == 1:
                count += 1
        # 열을 돌면서 1인 것들 카운트
        for i in range(1, col):
            if board[0][i] == 1:
                count += 1
        # 마지막 +2
        print("check3 count:", count + 2)
        return count + 2
    
    def check4(): # 0,0 -> 0일때 열을 돌리는 경우
        count = 0
        for i in range(1, col): # 0행의 열들 보면서 0인거 돌리기
            if board[0][i] == 0:
                count += 1
        for i in range(1, row): # 0열의 1인거 세기
            if board[i][0] == 1:
                count += 1
        
        # 마지막 +1
        print("check4 count:", count + 1)
        return count + 1
    
    def check5(): # 0,0 -> 0일때 행 돌리는 경우
        count = 0
        for i in range(1, row):
            if board[i][0] == 0:
                count += 1
        for i in range(1, col): # 0행의 1인거 세기
            if board[0][i] == 1:
                count += 1
        
        print("check5 count:", count + 1)
        return count + 1
    
    def check():
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0:
                    return False
        return True
    
    answer = check1()
    for i in board:
        print(i)
    
    print("answer:", answer)
    if answer == -1:
        return answer
    else:
        if board[0][0] == 1:
            return min(answer, min(check2(), check3()))
        else:
            return min(answer, min(check4(), check5()))
    
    return answer