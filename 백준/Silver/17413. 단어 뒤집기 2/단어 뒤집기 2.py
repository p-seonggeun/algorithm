s = input()
l = []
answer = ''
stack = []

for i in range(len(s)) :
    if s[i] == ' ' :
        if '<' not in stack :
            while l :
                answer += l.pop()
            answer += s[i]
        else :
            l.append(s[i])
    
    elif s[i] == '>' :
        while l :
            answer += l.pop(0)
        stack.pop()
        answer += s[i]
    
    else :
        if s[i] != '<' :
            l.append(s[i])
    
    if s[i] == '<' :
        while l :
            answer += l.pop()
        answer += s[i]
        stack.append(s[i])
    

while l :
    answer += l.pop()

print(answer)