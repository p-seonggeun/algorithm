def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for index, i in enumerate(citations) :
        if i <= index :
            return index
    
    return len(citations)