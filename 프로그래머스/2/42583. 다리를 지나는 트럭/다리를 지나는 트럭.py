def solution(bridge_length, weight, truck_weights) :
    answer = 0
    queue = [0] * bridge_length
    s = 0
    
    while queue :
        s -= queue.pop(0)
        if truck_weights :
            if s + truck_weights[0] <= weight :
                s += truck_weights[0]
                queue.append(truck_weights.pop(0))
            else :
                queue.append(0)
        answer += 1
        
    return answer