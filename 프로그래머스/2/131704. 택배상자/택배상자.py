def solution(order):
    answer = 0
    final = []
    middle = []
    count = 0
    
    for i in range(1, len(order) + 1) :
        if i != order[count] :
            middle.append(i)
        else :
            final.append(i)
            count += 1
            while middle and middle[-1] == order[count] :
                final.append(middle.pop())
                count += 1
    
    while middle and middle[-1] == order[count] :
        final.append(middle.pop())
        count += 1
    
    return len(final)
