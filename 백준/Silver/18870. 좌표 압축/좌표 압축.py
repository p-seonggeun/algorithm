import sys
import copy
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
temp_l = copy.deepcopy(l)
l = list(set(l))
dict = {}
l.sort()

for i in range(len(l)) :
    dict[l[i]] = i

for i in temp_l :
    print(dict[i], end = " ")