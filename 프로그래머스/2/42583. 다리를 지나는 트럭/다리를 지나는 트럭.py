def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = [0] * bridge_length
    s = sum(q)
    time = 0
    
    while q :
        s -= q.pop(0)
        if truck_weights :
            if s + truck_weights[0] <= weight :
                s = s + truck_weights[0]
                q.append(truck_weights.pop(0))
            else :
                q.append(0)
        time += 1
    answer = time
    return answer