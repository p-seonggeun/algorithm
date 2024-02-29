def solution(arr, query):
    answer = []
    for index, i in enumerate(query) :
        if index % 2 == 0 :
            arr = arr[:i + 1]
        else :
            arr = arr[i:]
    answer = arr
    return answer