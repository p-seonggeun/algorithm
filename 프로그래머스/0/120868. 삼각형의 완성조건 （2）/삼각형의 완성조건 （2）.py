def solution(sides):
    answer = 0
    sides.sort()
    side0 = sides[0]
    side1 = sides[1]
    side2 = side1 - side0 + 1
    
    # side1이 가장 긴 경우
    while (side1 < side0 + side2) and side2 <= side1 :
        answer += 1
        side2 += 1
    
    side2 = side1 + 1
    
    # side2이 가장 긴 경우
    while (side2 < side0 + side1) :
        answer += 1
        side2 += 1
    
    return answer