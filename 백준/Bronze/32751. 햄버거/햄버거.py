N = int(input())
A, B, C, D = map(int, input().split())
S = input()
d = {'a': A, 'b': B, 'c': C, 'd': D}

def check2():
    if S[0] == 'a' and S[-1] == 'a':
        return True
    return False


def check3():
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            return False
    return True


def check4():
    for i in S:
        if i in d:
            if d[i] - 1 < 0:
                return False
            d[i] -= 1
        else:
            return False
    return True

if check2() and check3() and check4():
    print("Yes")
else:
    print("No")