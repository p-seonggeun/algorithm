def solution(str1, str2):
    answer = 0
    a = []
    for i in range(len(str1) - 1):
        if not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        a.append(str1[i:i+2].lower())
    
    b = []
    for i in range(len(str2) - 1):
        if not str2[i].isalpha() or not str2[i+1].isalpha():
            continue
        b.append(str2[i:i+2].lower())
    
    print(a, b)
    
    if len(a) == len(b) == 0:
        return 65536
    c = {}
    d = {}
    
    for i in a:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    for i in b:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(c, d)
    
    e = set()
    for i in a + b:
        e.add(i)
    print(e)
    
    a = 0
    b = 0
    for i in e:
        if i in c and i in d:
            a += min(c[i], d[i])
    for i in e:
        if i in c and i in d:
            b += max(c[i], d[i])
        elif i in c:
            b += c[i]
        elif i in d:
            b += d[i]
            
    answer = int((a / b) * 65536)
    return answer