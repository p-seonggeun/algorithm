def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_list = {}
    report_count = {}
    for i in id_list :
        report_count[i] = 0
        report_list[i] = []
    
    for i in report :
        temp = i.split(" ")
        if temp[1] not in report_list[temp[0]] :
            report_list[temp[0]].append(temp[1])
            report_count[temp[1]] += 1
    
    temp = list(report_count.items())
    for i, j in temp :
        if j < k :
            report_count.pop(i)
    
    for i, j in enumerate(list(report_list.values())) :
        for k in j :
            if k in report_count :
                answer[i] += 1
    return answer