def solution(n, words):
    answer = []
    s = set()
    l = []
    for index, i in enumerate(words) :
        if not s and not l :
            l.append(i)
            s.add(i)
            continue
        if i in s :
            return [index % n + 1,  index // n + 1]
        else :
            if l[-1][-1] == i[0] :
                l.append(i)
                s.add(i)
            else :
                return [index % n + 1,  index // n + 1]
    else :
        return [0, 0]