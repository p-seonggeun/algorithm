a, b, c = map(int, input().split())
l = sorted([a, b, c])
long = l[0] + l[1] - 1
if l[-1] <= long : 
    long = l[-1]

print(long + l[0] + l[1])