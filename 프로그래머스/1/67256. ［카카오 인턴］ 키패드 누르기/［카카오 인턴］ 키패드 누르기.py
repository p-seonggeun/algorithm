def solution(numbers, hand):
    answer = ''
    pad = { '1' : [0, 0], '2' : [0, 1], '3' : [0, 2],
          '4' : [1, 0], '5' : [1, 1], '6' : [1, 2],
          '7' : [2, 0], '8' : [2, 1], '9' : [2, 2],
          '*' : [3, 0], '0' : [3, 1], '#' : [3, 2] }
    left = pad['*']
    right = pad['#']
    
    for i in numbers :
        i = str(i)
        if i == '1' or i == '4' or i == '7' :
            answer += 'L'
            left = pad[i]
        elif i == '3' or i == '6' or i == '9' :
            answer += 'R'
            right = pad[i]
        else :
            left_x, left_y = left
            right_x, right_y = right
            i_x, i_y = pad[i]
            d_l = abs(left_x - i_x) + abs(left_y - i_y)
            d_r = abs(right_x - i_x) + abs(right_y - i_y)
            if d_l > d_r : # 오른손이 더 가까움
                answer += 'R'
                right = pad[i]
            elif d_l < d_r :
                answer += 'L'
                left = pad[i]
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = pad[i]
                else :
                    answer += 'L'
                    left = pad[i]
    
    return answer