T = int(input())
l = list(map(int, input().split()))

def check(num):
    temp = 0
    for i in range(1, num):
        if num % i == 0:
            temp += i

    if num == temp:
        return "Perfect"
    elif num < temp:
        return "Abundant"
    else:
        return "Deficient"


for i in l:
    print(check(i))