N = int(input())
star = 2 * N + 1
space = -1
for i in range(0, 2 * N - 1) :
    
    if i < N :
        space += 1
        star = star - 2
    else :
        space -= 1
        star = star + 2
    print(space * " ", end = "")
    print(star * "*")