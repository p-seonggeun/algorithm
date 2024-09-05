from math import gcd
def solution(weights):
    answer = 0
    d = {}
    for i in weights :
        if i in d : d[i] += 1
        else : d[i] = 1
    
    key = list(d.keys())
    key.sort()
    s = {(2, 3), (1, 2), (3, 4)}
    for i in d :
        if d[i] >= 2 :
            answer += (d[i] * (d[i] - 1)) // 2
    
    for i in range(len(key)) :
        for j in range(i + 1, len(key)) :
            g = gcd(key[i], key[j])
            if ((key[i] // g) * key[j]) == ((key[j] // g) * key[i]) and (key[i] // g, key[j] // g) in s:
                print(key[i], key[j], key[i] // g, key[j] // g)
                answer += d[key[i]] * d[key[j]]
    
    return answer