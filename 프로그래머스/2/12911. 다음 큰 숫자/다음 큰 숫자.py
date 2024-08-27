def solution(n):
    answer = 0
    for i in range(n + 1, 1000001) :
        if str(bin(n)).count('1') == str(bin(i)).count('1') :
            answer = i
            break
    return answer