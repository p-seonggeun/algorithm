def solution(cards1, cards2, goal):
    answer = ''
    cards1.reverse()
    cards2.reverse()
    goal.reverse()
    
    while True:
        if not goal :
            return "Yes"
        if cards1 and cards1[-1] == goal[-1] :
            cards1.pop()
            goal.pop()
            continue
        if cards2 and cards2[-1] == goal[-1] :
            cards2.pop()
            goal.pop()
            continue
        return "No"