n = int(input())
l = list(map(int, input().split()))
r = [i + 1 for i in range(n)]

r[0], r[l[0]] = r[l[0]], r[0]

for i in range(n) : # 0 1 2 ... n - 1 // n번
    num = i + 1 # num = 1부터 n까지
    pre = l[i] # 1번부터 내 앞에 있는 수
    index = r.index(num)
    count = 0
    k = 0
    temp = 0
    for j in range(index) :
        if num < r[j] :
            count += 1 
    if count == pre : # 제 위치에 있는 경우
        # print("제 위치")
        continue
    elif count < pre : # 내 앞에 있는 수가 실제 앞에 있는 수보다 더 많은 경우 -> 뒤로 가야하는 경우
        # print("뒤로 가야하는 경우", num, pre - count)
        while k != pre - count :
            if r[index] < r[index + temp] :
                temp += 1
                k += 1
            else :
                temp += 1
        # print(temp)
        r[index], r[index + temp - 1] = r[index + temp - 1], r[index]
            
    else : # 앞으로 가야하는 경우
        # print("앞으로 가야하는 경우", num, count - pre)
        while k != count - pre:
            if r[index] < r[index - temp] :
                temp += 1
                k += 1
            else :
                temp += 1
        r[index], r[index - temp + 1] = r[index - temp + 1], r[index]
    # print(r)

for i in r :
    print(i, end = " ")