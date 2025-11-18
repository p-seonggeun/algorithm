# OX표 채점하기
# 1 ~ N 문제 순으로 채점됨
# i번 문제 점수 = i
# 보너스점수는 처음엔 0, 맞추면 1점 증가, 틀리면 초기화

N = int(input())
S = input().rstrip()

bonus = 0
answer = 0

for index, i in enumerate(S):
    if i == 'O':
        answer += (index + 1)
        answer += bonus
        bonus += 1
    else:
        bonus = 0

print(answer)