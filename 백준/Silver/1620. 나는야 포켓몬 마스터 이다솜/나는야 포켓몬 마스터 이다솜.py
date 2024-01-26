import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(n) :
    pm = input().rstrip()
    dict[pm] = i + 1

pm_list = list(dict.keys())

for _ in range(m) : 
    find = input().rstrip()
    if find.isalpha() :
        print(dict[find])
    else :
        print(pm_list[int(find) - 1])