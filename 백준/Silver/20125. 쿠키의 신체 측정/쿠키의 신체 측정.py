import sys
input = sys.stdin.readline

N = int(input())
c = []
for _ in range(N) :
    c.append(list(input().rstrip()))

def find_head() :
    for i in range(N) :
        for j in range(N) :
            if c[i][j] == '*' :
                head = [i, j]
                heart = [i + 1, j]
                return head, heart

head, heart = find_head()
left_arm, right_arm = 0, 0
left_leg, right_leg = 0, 0
height = 0
for index, i in enumerate(c[heart[0]]) :
    if index < heart[1] and i == '*' :
        left_arm += 1
    elif index > heart[1] and i == '*' :
        right_arm += 1

for i in range(heart[0] + 1, N) :
    if c[i][heart[1]] == '*' :
        height += 1

for i in range(heart[0] + height, N) :
    if c[i][heart[1] - 1] == '*' :
        left_leg += 1

for i in range(heart[0] + height, N) :
    if c[i][heart[1] + 1] == '*' :
        right_leg += 1

heart = [i + 1 for i in heart]
print(*heart)
print(left_arm, right_arm, height, left_leg, right_leg)