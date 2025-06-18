N = int(input())
l = []

def is_prime(num) :
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True

def dfs(count) :
    if count > N :
        return
    if count == N :
        print(''.join(map(str, l)))
        return

    for i in range(1, 10) :
        l.append(i)
        if is_prime(int(''.join(map(str, l)))):
            dfs(count + 1)
        l.pop()

dfs(0)