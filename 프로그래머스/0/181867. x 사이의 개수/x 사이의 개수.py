def solution(myString):
    answer = []
    temp = myString.split("x")
    for i in temp :
        answer.append(len(i))
    return answer