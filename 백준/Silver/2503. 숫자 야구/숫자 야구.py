N = int(input())
answer = 0
number = []
strike = []
ball = []

def count_strike(num1, num2) :
    count = 0
    for i in range(3) :
        if str(num1)[i] == str(num2)[i] :
            count += 1
    return count

def count_ball(num1, num2) :
    count = 0
    l = list(str(num2))
    for i in range(3) :
        if str(num1)[i] != str(num2)[i] and str(num1)[i] in l:
            count += 1
    return count

for _ in range(N):
    num, a, b = map(int, input().split())

    number.append(num)
    strike.append(a)
    ball.append(b)

for i in range(100, 1000) :
    flag = True
    for a, b, c in zip(number, strike, ball) :
        if count_strike(i, a) != b or count_ball(i, a) != c :
            flag = False

    if flag :
        if '0' not in str(i) and len(str(i)) == len(set(str(i))):
            answer += 1
print(answer)
