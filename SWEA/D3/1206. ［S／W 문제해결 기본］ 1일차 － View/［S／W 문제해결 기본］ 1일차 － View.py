#import sys
#sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1) :
    N = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for i in range(len(height)) :
        temp = []
        flag = True
        if height[i] == 0 : continue
        for j in range(-2, 3) :
            if j == 0 : continue
            if height[i] - height[i + j] <= 0 : 
                flag = False
                break
            temp.append(height[i] - height[i + j])
        if flag : 
            answer += min(temp)
    
    print(f'#{tc}', answer)