def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :
        temp = bin(int(bin(i)[2:], 2) | int(bin(j)[2:], 2))[2:]
        s = ''
        if len(temp) != n :
            temp = (n - len(temp)) * '0' + temp
        for i in temp :
            if i == '1' :
                s += '#'
            else :
                s += ' '
        answer.append(s)
    return answer