from heapq import *

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (원소들에 -1을 곱하여 최소 힙으로 구현)
    d = {} # 숫자의 개수를 나타내는 dictionary
    for i in operations:
        sign, data = i.split(" ")
        data = int(data)
        if sign == 'I': # 숫자 삽입
            heappush(min_heap, data)
            heappush(max_heap, -data)
            if data in d:
                d[data] += 1
            else:
                d[data] = 1
                
        elif min_heap and data == -1: # 최솟값 제거
            while min_heap: # 실제 존재하는 최솟값이 나올 때까지 최소 힙에서 원소를 꺼낸다.
                result = heappop(min_heap)
                if d[result] > 0:
                    d[result] -= 1
                    break
                    
        elif max_heap: # 최댓값 제거
            while max_heap: # 실제 존재하는 최댓값이 나올 때까지 최대 힙에서 원소를 꺼낸다.
                result = -heappop(max_heap)
                if d[result] > 0:
                    d[result] -= 1
                    break
                    
    if min_heap == [] or max_heap == []: # 힙이 비어있을 경우
        return [0, 0]
    min_val, max_val = min_heap[0], max_heap[0]
    while min_heap: # 실제 존재하는 최솟값이 나올 때까지 최소 힙에서 원소를 꺼낸다.
        min_val = heappop(min_heap)
        if d[min_val] > 0:
            break
    while max_heap: # 실제 존재하는 최댓값이 나올 때까지 최대 힙에서 원소를 꺼낸다.
        max_val = -heappop(max_heap)
        if d[max_val] > 0:
            break
    return [max_val, min_val]