N = int(input())
for i in range(1, N + 1):
    l = list(input().rstrip().split(" "))
    l.reverse()
    t = ""
    for j in l:
        t += j + " "
    print(f"Case #{i}: {t}")