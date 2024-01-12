import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.insert(0, 0)

acc_l = [0] * (len(l) + 1)
acc_l[0] = 0
acc_l[1] = l[0]

for i in range(1, len(l)) :
    acc_l[i] = l[i] + acc_l[i - 1]

for _ in range(m) :
    i, j = map(int, input().split())
    print(acc_l[j] - acc_l[i - 1])