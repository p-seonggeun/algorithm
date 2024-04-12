import sys
from itertools import product
input = sys.stdin.readline
N = input().rstrip()
M = int(input())
temp = [str(i) for i in range(10)]
if M != 0 : 
    l = set(map(str, input().split()))
    temp = [str(i) for i in range(10) if str(i) not in l]
else :
    l = set()

if int(N) == 100 :
    print(0)
    exit(0)

answer = 1e12
for j in range(1, 7) :
    for i in list(product(temp, repeat = j)) :
        answer = min(answer, abs(int(N) - int(''.join(i))) + len(str(int(''.join(i)))))

print(min(answer, abs(int(N) - 100)))