N = int(input())
ball = input().rstrip()

def left_red(balls) :
    count = 0
    flag = False
    for index, i in enumerate(balls) :
        if i == 'B' :
            flag = True
            continue
        if flag == True :
            if i == 'R' :
                count += 1
    return count

def left_blue(balls) :
    count = 0
    flag = False
    for index, i in enumerate(balls) :
        if i == 'R' :
            flag = True
            continue
        if flag == True :
            if i == 'B' :
                count += 1
    return count

def right_red(balls) :
    count = 0
    flag = False
    for i in range(len(balls) - 1, -1, -1) :
        if balls[i] == 'B' :
            flag = True
            continue
        if flag == True :
            if balls[i] == 'R' :
                count += 1
    return count


def right_blue(balls) :
    count = 0
    flag = False
    for i in range(len(balls) - 1, -1, -1) :
        if balls[i] == 'R' :
            flag = True
            continue
        if flag == True :
            if balls[i] == 'B' :
                count += 1
    return count

print(min(left_red(ball), left_blue(ball), right_red(ball), right_blue(ball)))