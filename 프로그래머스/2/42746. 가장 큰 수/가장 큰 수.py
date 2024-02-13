def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key = lambda x : (x * 4)[:4], reverse = True)
    
    answer = ''.join(numbers)
    
    if answer[0] == '0':
        return '0'
    else:
        return answer