def solution(dots):
    answer = 0
    dots.sort()
        
    x1, y1 = dots[0][0], dots[0][1]
    x2, y2 = dots[-1][0], dots[-1][1]
    
    answer = (x2 - x1) * (y2 - y1)
    
    return answer