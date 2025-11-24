def solution(board, moves):
    answer = 0
    b = []
    # moves 만큼 반복하기
    for move in moves:
        # 0행, move 열부터 
        c = move - 1
        for r in range(len(board)):
            if board[r][c] != 0:
                print(board[r][c])
                if not b:
                    b.append(board[r][c])
                else:
                    if b[-1] == board[r][c]:
                        b.pop()
                        answer += 2
                    else:
                        b.append(board[r][c])
                board[r][c] = 0
                break
    return answer