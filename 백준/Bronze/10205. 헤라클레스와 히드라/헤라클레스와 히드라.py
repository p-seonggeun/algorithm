K = int(input())
for k in range(K) :
    h = int(input())
    s = input().rstrip()

    for i in s :
        if h <= 0 :
            break
        if i == 'b' : h -= 1
        elif i == 'c' : h += 1

    print(f"Data Set {k + 1}:")
    print(h)
    print()