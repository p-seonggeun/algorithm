def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print(new_id)
    # 2단계
    temp = ''
    for i in new_id :
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.' :
            temp += i
    new_id = temp
    print(new_id)
    
    # 3단계
    while '..' in new_id :
        new_id = new_id.replace("..", ".")
    print(new_id)
    
    # 4단계
    new_id = new_id.lstrip(".")
    new_id = new_id.rstrip(".")
    print(new_id)
    
    # 5단계
    if new_id == '' :
        new_id += 'a'
    print(new_id)
    
    # 6단계
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.' :
            new_id = new_id[:14]
    print(new_id)
    
    # 7단계
    if len(new_id) <= 2 :
        while len(new_id) != 3 :
            new_id += new_id[-1]
    print(new_id)
    
    answer = new_id
    return answer