def solution(myString):
    answer = []
    temp = myString.split("x")
    l = []
    for i in temp :
        if i != "" :
            l.append(i)
    l.sort()
    answer = l
    return answer