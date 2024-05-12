from collections import Counter
#import sys

#sys.stdin = open("input.txt", "r")
T = int(input())

for i in range(1, T + 1) :
    N = int(input())
    score = list(map(int, input().split()))

    temp = (list(Counter(score).items()))
    temp.sort(key = lambda x : (-x[1], -x[0]))
    print(f"#{i}", temp[0][0])