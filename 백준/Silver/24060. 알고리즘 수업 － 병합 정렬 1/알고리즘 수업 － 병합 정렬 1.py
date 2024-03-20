import math
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
array = list(map(int, input().split()))
global cnt
cnt = 0
answer = []
def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = math.ceil(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]

    m_left = merge_sort(left)
    m_right = merge_sort(right)

    return merge(m_left, m_right)

def merge(left, right) :
    global cnt
    i, j = 0, 0
    sorted_arr = []

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            sorted_arr.append(left[i])
            answer.append(left[i])
            cnt += 1
            i += 1
        else :
            sorted_arr.append(right[j])
            answer.append(right[j])
            cnt += 1
            j += 1
    
    while i < len(left) :
        sorted_arr.append(left[i])
        answer.append(left[i])
        cnt += 1
        i += 1
    while j < len(right) :
        answer.append(right[j])
        sorted_arr.append(right[j])
        cnt += 1
        j += 1
    return sorted_arr

merge_sort(array)

if cnt < k :
    print(-1)
else :
    print(answer[k - 1])