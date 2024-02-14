while True :
    n = int(input())
    if n == -1 :
        break
    l = [i for i in range(1, n) if n % i == 0]
    
    if sum(l) == n :
        print(n, "= ", end = "")
        print(*l, sep = " + ")
    else :
        print(n, "is NOT perfect.")