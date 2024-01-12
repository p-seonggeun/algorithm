a, b, c = map(int, input().split())

def multi(a, b, c) :
    if b == 1 :
        return a % c
    else :
        if b % 2 != 0 :
            return ((multi(a, b // 2, c) ** 2) * a) % c
        else :
            return (multi(a, b // 2, c) ** 2) % c
        
print(multi(a, b, c))