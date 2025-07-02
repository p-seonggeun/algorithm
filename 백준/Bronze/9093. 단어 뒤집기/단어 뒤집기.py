T = int(input())
for _ in range(T):
    l = input().split()
    for i in l:
        t = list(i)
        t.reverse()
        print(''.join(t), end =" ")
    print()