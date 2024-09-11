from functools import reduce
def xor(a, b) :
    return a ^ b

def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    
    s = []
    for i in range(row_begin, row_end + 1) :
        t = 0
        for j in range(len(data[i - 1])) :
            t += data[i - 1][j] % i
        s.append(t)
    
    answer = reduce(xor, s)
    return answer