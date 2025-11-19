N = int(input())

dp = [0] * 31
dp[0] = 1
dp[1] = 1

for i in range(2, 31):
    dp[i] = dp[i - 1] * i

flag = False
while dp:
    num = dp.pop()

    if num > N:
        continue
    else:
        N -= num

    if N == 0:
        flag = True
        break
    elif N < 0:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
