# 각각의 손님이 주문한 메뉴들로 만들 수 있는 조합 만들기
# 조합을 만들때 개수는 course와 같게끔
# 코스가 2, 3, 4가 들어있으면 2개, 3개, 4개 조합 만들기
# 딕셔너리 아이템으로 뽑기 ?
# combinatons가 가능한가 ?
from itertools import combinations
def solution(orders, course):
    answer = []
    l = []
    dict = {}
    for i in orders :
        i = list(i)
        i.sort()
        i = ''.join(i)
        for j in course :
            if len(i) < j :
                continue
            l.append(list(combinations(i, j)))
            
    for i in l :
        for j in i :
            if j in dict :
                dict[j] += 1
            else :
                dict[j] = 1
                
    temp = []
    for i, j in dict.items() :
        temp.append((i, j))
    
    temp.sort(key = lambda x : (-len(x[0]), x[1]), reverse = True)
    
    temp3 = []
    for i in course :
        temp2 = []
        for j in temp :
            if i == len(j[0]) :
                if j[1] >= 2 :
                    if not temp2 :
                        temp2.append((i, j))
                    else :
                        if temp2[-1][-1][-1] == j[1] :
                            temp2.append((i, j))
        if temp2 :
            temp3.append(temp2)
    
    for i in temp3 :
        for j in i :
            answer.append(''.join(j[1][0]))
    
    answer.sort()
                
    return answer