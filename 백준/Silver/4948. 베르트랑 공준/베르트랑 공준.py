l = [True] * (123456 * 2 + 1)
l[0] = False
l[1] = False
for i in range(2, 123456 * 2) :
    if l[i] == True :
        for j in range(i + i, 123456 * 2 + 1, i) :
            l[j] = False

while True :
    n = int(input())
    if n == 0 :
        break
    count = 0
    
    for i in range(n + 1, (n * 2) + 1) :
        if l[i] == True :
            count += 1

    print(count)