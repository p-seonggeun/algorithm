#import sys
#sys.stdin = open("input.txt", "r")

N = int(input())

for i in range(1, N + 1) :
    flag = True
    temp = ''
    for j in str(i) :
        if int(j) % 3 == 0 and j != '0' :
            temp += '-'
            flag = False
    if flag :
        print(i, end = " ")
    else :
        print(temp, end = " ")