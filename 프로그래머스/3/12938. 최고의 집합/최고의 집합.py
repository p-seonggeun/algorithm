def solution(n, s):
    answer = []
    
    # s를 n개의 수로 나눈다
    temp = s // n
    if temp == 0:
        return [-1]
    
    l = []
    while len(l) != n:
        l.append(temp)
    
    rest = s - (temp * n)
    # 곱이 가장 크려면 원소간의 차이가 작아야한다
    index = 0
    while rest > 0:
        if index == n:
            index = 0
        l[index] += 1
        rest -= 1
        index += 1

    l.sort()
    answer = l
    return answer