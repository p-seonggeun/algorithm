from itertools import product
import math
import copy
def solution(users, emoticons):
    answer = []
    sale = [10, 20, 30, 40]
    sales = list(product(sale, repeat = len(emoticons)))
    l = []
    for i in users :
        i.append(0)
        i.append(0)
        
    for i in sales :
        copy_users = copy.deepcopy(users)
        e_plus, e_buy = 0, 0
        
        for j, k in zip(i, emoticons) :
            price = (k // 100 * (100 - j))
            
            for m in copy_users :
                if j >= m[0] :
                    m[3] += price
                    
                if m[2] != 1 and m[3] >= m[1] :
                    m[2] += 1
                    m[3] = 0
        
        for m in copy_users :
            if m[2] == 1 :
                e_plus += 1
            else :
                e_buy += m[3]
        l.append([e_plus, int(e_buy)])
    
    l.sort(key = lambda x : (x[0], x[1]), reverse = True)
    answer = l[0]
    return answer