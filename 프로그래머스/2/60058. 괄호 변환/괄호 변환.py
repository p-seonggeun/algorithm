def solution(p):
    answer = ''
    
    def split_string(sp_st) :
        dictionary = {}
        v_index = 0
        for index, i in enumerate(sp_st) :
            if i in dictionary :
                dictionary[i] += 1
            else :
                dictionary[i] = 1
        
            if len(list(dictionary.values())) != 1 :
                if dictionary['('] == dictionary[')'] :
                    v_index = index
                    break
        u, v = sp_st[:v_index + 1], sp_st[v_index + 1:]
        return u, v
    
    def check(ch_st) :
        stack = []
        for i in ch_st :
            if stack :
                if i == ')' :
                    if stack[-1] == '(' :
                        stack.pop()
                    else :
                        stack.append(i)
                else :
                    stack.append(i)
            else :
                stack.append(i)
        if stack :
            return False
        else :
            return True
        
    def reverse_string(re_st) :
        re_st.pop(0)
        re_st.pop(-1)
        if not re_st :
            return []
        else :
            for i in range(len(re_st)) :
                if re_st[i] == '(' :
                    re_st[i] = ')'
                else :
                    re_st[i] = '('
            return re_st
        
    def shoot(st) :
        if len(st) == 0 :
            return []
        u, v = split_string(st)
        if check(u) :
            return u + shoot(v)
        else :
            u = reverse_string(u)
            return ['('] + shoot(v) + [')'] + u
        
    return ''.join(shoot(list(p)))

