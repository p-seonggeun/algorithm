import sys
import math
input = sys.stdin.readline
def isPrime(n) :
    if n == 0 or n == 1 :
        return 2
    else :
        while True :
            flag = True
            for i in range(2, int(math.sqrt(n)) + 1) :
                if n % i == 0 :
                    flag = False
                    break
            if not flag :
                n += 1
            else :
                return n
t = int(input())

for _ in range(t) :
    print(isPrime(int(input())))
