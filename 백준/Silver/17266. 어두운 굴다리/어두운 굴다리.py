import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
X = list(map(int, input().split()))
answer = []
s, e = 0, N
if M != 1 :
    while s <= e :
        mid = ((s + e) // 2)
        flag = True
        for i in range(len(X)) :
            if i == 0 :
                if X[i] - mid <= 0 and X[i] + mid >= X[i + 1] - mid : continue
                else : flag = False

            elif i == len(X) - 1 :
                if X[i] - mid <= X[i - 1] + mid and X[i] + mid >= N : continue
                else : flag = False
            
            else :
                if X[i] - mid <= X[i - 1] + mid and X[i] + mid >= X[i + 1] - mid : continue
                else : flag = False

        if flag :
            answer.append(mid)
            e = mid - 1
        else :
            s = mid + 1
else :
    answer = [N]
print(min(answer))