def solution(arr):
    answer = []
    i = 0
    stk = []
    while i < len(arr) :
        if not stk :
            stk.append(arr[i])
            i += 1
        else :
            if stk[-1] == arr[i] :
                stk.pop()
                i += 1
            else :
                stk.append(arr[i])
                i += 1
    
    if len(stk) == 0 :
        return [-1]
    answer = stk
    
    return answer