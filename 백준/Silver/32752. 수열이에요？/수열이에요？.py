N, L, R = map(int, input().split())
A = list(map(int, input().split()))

L -= 1
R -= 1

temp = A[L:R + 1]
temp.sort()

t = (A[:L] + temp + A[R + 1:])

flag = True
for i in range(len(A) - 1):
    if t[i] > t[i + 1]:
        print(0)
        break
else:
    print(1)
