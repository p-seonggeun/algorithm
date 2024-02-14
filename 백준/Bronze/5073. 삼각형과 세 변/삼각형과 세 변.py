while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    l = sorted([a, b, c])
    if l[-1] < l[0] + l[1] :
        if a == b == c :
            print("Equilateral")
        elif a == b or a == c or b == c :
            print("Isosceles")
        elif a != b != c :
            print("Scalene")
    else :
        print("Invalid")
    