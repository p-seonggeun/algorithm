import sys
input = sys.stdin.readline

m, n = map(int, input().split())
l = list(map(int, input().split()))

start = 1
end = max(l)

while (start <= end) :
    total = 0
    mid = (start + end) // 2

    for i in l :
        total += (i // mid)
    
    if total >= m :
        start = mid + 1
    else :
        end = mid - 1

print(end)