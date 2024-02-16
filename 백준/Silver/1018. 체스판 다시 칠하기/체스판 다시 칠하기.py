n, m = map(int, input().split())
count = 1e9
w = [["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"]]

b = [["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"],
     ["B", "W", "B", "W", "B", "W", "B", "W"],
     ["W", "B", "W", "B", "W", "B", "W", "B"]]

l = []
for _ in range(n) :
    l.append(list(input()))

for k in range(n - 7) :
    for p in range(m - 7) :
        w_count = 0
        b_count = 0
        for i in range(8) :
            for j in range(8) :
                if l[k + i][p + j] == w[i][j] :
                    w_count += 1
                if l[k + i][p + j] == b[i][j] :
                    b_count += 1
        count = min(count, w_count, b_count)

print(count)