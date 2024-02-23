def solution(number):
    answer = 0
    number = str(number)
    temp = 0
    for i in number :
        temp += int(i)
    answer = temp % 9 
    return answer