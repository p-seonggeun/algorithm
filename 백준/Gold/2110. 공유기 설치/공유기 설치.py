import sys
input = sys.stdin.readline

N, C = map(int, input().split())
l = []
for _ in range(N) :
    l.append(int(input()))

l.sort()

start = 1
end = l[-1] - l[0]

result = 0
while (start <= end) :
    mid = (start + end) // 2
    
    temp = 1
    last = l[0]
    for i in range(1, len(l)) :
        if last + mid <= l[i] :
            temp += 1
            last = l[i]

    if temp >= C :
        start = mid + 1
        if (mid > result) :
            result = mid
    else :
        end = mid - 1

print(result)