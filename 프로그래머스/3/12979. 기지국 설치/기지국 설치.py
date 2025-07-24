from collections import deque
def solution(n, stations, w):
    answer = 0
    # w가 1일때 3칸
    # n에 박는순간 n - w, n + w까지 커버
    # 만약에 3에 박고 w가 2이면 1~5까지 커버
    index = 1
    queue = deque(stations)
    p = queue.popleft()
    while index <= n:
        if index < p - w or index > p + w:
            answer += 1
            index += 2 * w + 1
        elif p - w <= index <= p + w:
            index = p + w + 1
            if queue:
                p = queue.popleft()
    # index가 1부터 시작해서 N보다 같거나 작을동안만 계속진행

    # 이미 박혀있는곳은?
    # 스테이션을 큐로 만들어서 하나씩 꺼내기
    # 하나씩 꺼낸거보다 index가 작다면?
    # answer += 1 하고 index += 2 * w + 1
    # index가 사이에 있다면?
    # index = 최대커버 + 1까지 이동
    # index가 더 크다면?
    
    return answer