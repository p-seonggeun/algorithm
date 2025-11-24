answer = 0
temp = []
last = []
def solution(user_id, banned_id):
    def dfs(index):
        global answer, temp, last
        if len(temp) == len(banned_id):
            t = sorted(temp)
            if t not in last:
                last.append(t)
                answer += 1
            return
        
        for i in range(len(user_id)):
            if len(user_id[i]) == len(banned_id[len(temp)]):
                # print(user_id[i], banned_id[len(temp)])
                for j in range(len(user_id[i])):
                    if banned_id[len(temp)][j] == '*':
                        continue
                    else:
                        if user_id[i][j] != banned_id[len(temp)][j]:
                            break
                else:
                    if user_id[i] not in temp:
                        temp.append(user_id[i])
                        dfs(index + 1)      
                        temp.pop()
    
    dfs(0)  
                
    return answer