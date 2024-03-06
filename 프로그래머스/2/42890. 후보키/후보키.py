from collections import Counter
from itertools import combinations
def solution(relation):
    answer = 0
    column = len(relation[0])
    row = len(relation)
    rotate = [[] for i in range(column)]
    length_key = [[] for i in range(column + 1)]
    dictionary = {}
    comlist = []
    key_set = set()
    for i in range(column) :
        for j in range(row) :
            rotate[i].append(relation[j][i])
    
    for index, i in enumerate(rotate) :
        comlist.append(index)
    
    for i in range(1, column + 1) :
        d = []
        for j in (list(combinations(comlist, i))) :
            s = []
            for l in range(row) :
                t = ''
                for k in j :
                    t += relation[l][k]
                s.append(t)
            temp_list = list(set(Counter(s).values()))
            if len(temp_list) == 1 and temp_list[0] == 1 :
                if len(key_set) == 0 :
                    if len(j) == 1 :
                        j = j[0]
                    key_set.add(j)
                else :
                    flag = True
                    for p in key_set :
                        if isinstance(p, tuple) :
                            p = set(p)
                            j = set(j)
                            if p.issubset(j) :
                                flag = False
                                break
                        if p in j :
                            flag = False
                            break
                    if flag :
                        key_set.add(tuple(j))
            d.append(s)
    
    answer = len(key_set)

#     for i in range(row) : # 행
#         for j in range(1, column + 1) : # 몇개 뽑을지
#             for k in range(column - j + 1) : # 시작위치
#                 insert = relation[i][k : k + j]
#                 length_key[len(insert)].append(insert)
    
#     for i in length_key :
#         print(i)
    
    return answer