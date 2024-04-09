from collections import deque
N, K = map(int, input().split())
belt = list(map(int, input().split()))
belt = deque(belt)
robot = deque([0] * (2 * N))
answer = 0
cnt = 0
flag = True
while flag :
    # 1. 벨트와 로봇 회전
    belt.rotate(1) # 오른쪽으로 회전
    robot.rotate(1)
    if robot[N - 1] == 1 :
        robot[N - 1] = 0

    # 2. 맨 먼저 올라간 로봇부터 한칸 이동
    # 로봇없어야되고, 내구도 남아있어야되고, 내리는 곳(N)이면 바로 내려야함
    for i in range(N - 2, -1, -1) :
        if robot[i] == 1 :
            if robot[i + 1] == 0 and belt[i + 1] >= 1 :
                robot[i + 1], robot[i] = robot[i], robot[i + 1]
                belt[i + 1] -= 1
                if belt[i + 1] == 0 :
                    cnt += 1
                if i + 1 == N - 1 :
                    if robot[i + 1] == 1 :
                        robot[i + 1] = 0
            else :
                continue           

    # 3. 로봇 올리기
    if belt[0] > 0 :
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0 :
            cnt += 1

    # 4. 내구도 확인
    if cnt >= K :
        flag = False
    answer += 1

print(answer)