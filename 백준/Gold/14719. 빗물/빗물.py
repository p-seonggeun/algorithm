# 가장 긴 기둥이
# 오른쪽
# 맨왼쪽에서부터 가장 긴 기둥까지 하나씩 반복
# 0이거나, 물이 차오르는 리스트에 잇으면 건너뜀
# 아니면 나보다 같거나, 크거나, 맨 오른쪽까지
# 그러면 높이차를 계산

# 왼쪽

# 가운데
# 맨 왼쪽에서부터 가운데까지
# 맨 왼쪽에서 쏘면 나보다 낮아야 물이 차오름 나보다 크거나 같은걸 만나면 멈춤
# 내가 0이면 건너뜀
# 나보다 작으면 물이 나와 그 위치의 높이 차이만큼 물이 차오름(물이 차오르는 지점을 저장해두고 물이 차오르는 지점 반복 위치일때 건너뜀)

# 맨 오른쪽에서 부터 가운데까지

import sys
input = sys.stdin.readline
H, W = map(int, input().split())
height = list(map(int, input().split()))

standard = height.index(max(height))
check = set()
answer = 0

if standard == W - 1 : # 맨 오른쪽
    for index, i in enumerate(height) :
        if i == 0 or index in check :
            continue
        for j in range(index + 1, W) :
            if height[j] < i :
                check.add(j)
                answer += i - height[j]
            else :
                break

elif standard == 0 : # 맨 왼쪽
    for i in range(len(height) - 1, -1, -1) :
        if height[i] == 0 or i in check :
            continue
        for j in range(i - 1, -1, -1) :
            if height[j] < height[i] :
                check.add(j)
                answer += height[i] - height[j]
            else :
                break

else : # 가운데
    for i in range(standard) : # 왼쪽
        if height[i] == 0 or i in check :
            continue
        for j in range(i + 1, standard) :
            if height[j] < height[i] :
                check.add(j)
                answer += height[i] - height[j]
            else :
                break
    
    for i in range(len(height) -1, standard, -1) :
        if height[i] == 0 or i in check :
            continue
        for j in range(i - 1, standard, -1) :
            if height[j] < height[i] :
                check.add(j)
                answer += height[i] - height[j]
            else :
                break

print(answer)