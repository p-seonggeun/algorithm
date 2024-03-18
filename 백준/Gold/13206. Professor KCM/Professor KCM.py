import sys
import math
input = sys.stdin.readline

t = int(input())

for _ in range(t) :
    n = int(input())
    num = sorted(list(map(int, input().split())))

    for i in range(len(num) - 1) :
        num[i], num[i + 1] = math.gcd(num[i], num[i + 1]), math.lcm(num[i], num[i + 1])
    
    print(num[-1] % 1000000007)