def solution(keyinput, board):
    answer = []
    width = (board[0] - 1) // 2
    height = (board[1] - 1) // 2
    
    x, y = 0, 0
    for i in keyinput :
        move_x = 0
        move_y = 0
        if i == "left" :
            move_x = -1
        elif i == "right" :
            move_x = 1
        elif i == "up" :
            move_y = 1 
        elif i == "down" :
            move_y = -1 
        if x + move_x < -width or x + move_x > width or y + move_y < -height or y + move_y > height :
            continue
        else :
            x += move_x
            y += move_y
    answer = [x, y]
    return answer