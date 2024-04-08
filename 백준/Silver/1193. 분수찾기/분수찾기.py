n = int(input())

count = 0
lr = False # 왼

while True :
    count += 1
    if n > count :
        n -= count
    else :
        break
    if lr == False :
        lr = True
    else :
        lr = False

l, r = 0, 0

if lr == False :
    l = count
    r = 1
else :
    l = 1
    r = count

for i in range(n - 1) :
    if lr == False :
        l -= 1
        r += 1
    else :
        l += 1
        r -= 1

print(str(l) + '/' + str(r))