import sys
input = sys.stdin.readline

t = int(input())

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(t) :
    global cnt
    cnt = 0
    s = input().rstrip()
    if isPalindrome(s) :
        print(1, cnt)
    else :
        print(0, cnt)