def solution(chicken):
    answer = -1
    chick = []
    coupon, service = 0, -1
    coupon = chicken
    
    while (service != 0):
        service = coupon // 10
        coupon = coupon % 10 + service
        chick.append(service)
        
    answer = sum(chick)
    
    return answer