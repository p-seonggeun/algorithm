def calc(oper) :
    tc = []
    for i in oper :
        tc.append(i)
        if len(tc) == 3 :
            one = int(tc[0])
            two = tc[1]
            three = int(tc[2])
            if two == '+' :
                tc = [str(one + three)]
            elif two == '-':
                tc = [str(one - three)]
            elif two == '*' :
                tc = [str(one * three)]
            elif two == '/' :
                if one < 0 :
                    one = -1 * (one)
                    tc = [str(-1 * (one // three))]
                else :
                    tc = [str(one // three)]

    return tc

def make(t) :
    o = []
    for i, j in zip(A, t) :
        o.append(str(i))
        o.append(j)

    o.append(str(A[-1]))
    return calc(o)

def dfs(count) :
    global maxi, mini
    if count == N - 1 :
        ans = int(make(temp)[0])
        maxi = max(maxi, ans)
        mini = min(mini, ans)
        return

    for i in d :
        if d[i] > 0 :
            temp.append(i)
            d[i] -= 1
            dfs(count + 1)
            d[i] += 1
            temp.pop()

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
maxi = -10 ** 9
mini = 10 ** 9
temp = []
d = {'+' : op[0], '-' : op[1], '*' : op[2], '/' : op[3]}

dfs(0)
print(maxi)
print(mini)