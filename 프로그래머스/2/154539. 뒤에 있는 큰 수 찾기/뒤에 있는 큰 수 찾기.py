def solution(numbers):
    answer = []
    temp = []
    for i in range(len(numbers)) :
        if not temp :
            temp.append(numbers.pop())
            answer.append(-1)
        else :
            t = numbers.pop()
            if t < temp[-1] :
                answer.append(temp[-1])
                temp.append(t)
            else :
                while temp and t >= temp[-1] :
                    temp.pop()
                if temp :
                    answer.append(temp[-1])
                else :
                    answer.append(-1)
                temp.append(t)

    return answer[::-1]