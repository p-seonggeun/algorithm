n = int(input())
d = [0] + [1] * 9

for _ in range(n - 1) :
    pre = d[:]
    d[0] = pre[1]
    for i in range(1, 9) :
        d[i] = pre[i - 1] + pre[i + 1]
    d[9] = pre[8]

print(sum(d) % 1000000000)

# 0 1 2 3 4 5 6 7 8 9
# [10] [12] [21 23] [32 34] [43 45] [54 56] [65 67] [76 78] [87 89] [98]
# [101] [121 123] [210 212 232 234] [321 323 343 345] [432 434 454 456] [543 545 565 567] [654 656 676 678] [765 767 787 789] [876 878 898] [987 989]