from itertools import product
import math
import copy
def solution(users, emoticons):
    answer = []
    sale = [10, 20, 30, 40]
    sales = list(product(sale, repeat = len(emoticons)))
    l = []
        
    for i in sales :
        e_plus, e_buy = 0, 0
        for j in users :
            u_s, u_m = j[0], j[1]
            e, purchase = False, 0
            for k, m in zip(i, emoticons) :
                price = (m // 100 * (100 - k))
                if k >= u_s :
                    purchase += price
                if purchase >= u_m :
                    e = True
                    break
            if e :
                e_plus += 1
            else :
                e_buy += purchase
    
        l.append([e_plus, int(e_buy)])
    
    l.sort(key = lambda x : (x[0], x[1]), reverse = True)
    answer = l[0]
    return answer