import sys
input = sys.stdin.readline

prime_list = [True] * 1000001
prime_list[0] = False
prime_list[1] = False

for i in range(2, 1000001) :
    if prime_list[i] == True :
        for j in range(i + i, 1000001, i) :
            prime_list[j] = False

t = int(input())

for _ in range(t) :
    n = int(input())
    cnt = 0
    for i in range(2, n // 2 + 1) :
        if prime_list[i] == True :
            if prime_list[n - i] == True :
                    cnt += 1
    print(cnt)
