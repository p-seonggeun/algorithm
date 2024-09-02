import math
def solution(fees, records):
    answer = []
    parking_list = {}
    park_cost = {}
    for i in records :
        temp = i.split(" ")
        if temp[2] == "IN" :
            parking_list[temp[1]] = temp[0]
        else :
            park_car = parking_list.pop(temp[1])
            in_time = temp[0].split(":")
            out_time = park_car.split(":")
            hour = int(in_time[0]) - int(out_time[0])
            minute = int(in_time[1]) - int(out_time[1])
            if minute < 0 :
                while minute < 0 :
                    hour -= 1
                    minute += 60
            if temp[1] in park_cost :
                park_cost[temp[1]] += hour * 60 + minute
            else :
                park_cost[temp[1]] = hour * 60 + minute

    left_car = list(parking_list.items())
    for i in left_car : 
        in_time = i[1].split(":")
        hour = 23 - int(in_time[0])
        minute = 59 - int(in_time[1])
        if minute < 0 :
            while minute < 0 :
                hour -= 1
                minute += 60
        if i[0] in park_cost :
            park_cost[i[0]] += hour * 60 + minute
        else :    
            park_cost[i[0]] = hour * 60 + minute
    
    car_fee = list(park_cost.items())
    car_fee.sort(key = lambda x : x[0])
    for i in car_fee :
        if i[1] <= fees[0] :
            answer.append(fees[1])
        else :
            answer.append(fees[1] + (math.ceil((i[1] - fees[0]) / fees[2])) * fees[3])
    
    return answer