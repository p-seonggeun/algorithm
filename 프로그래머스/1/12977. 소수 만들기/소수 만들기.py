from itertools import combinations
def solution(nums):
    answer = 0
    
    def is_prime(num) :
        for i in range(2, int(num ** 0.5) + 1) :
            if num % i == 0 :
                return False
        return True
    
    for i in list(combinations(nums, 3)) :
        if (is_prime(sum(i))) :
            answer += 1

    return answer