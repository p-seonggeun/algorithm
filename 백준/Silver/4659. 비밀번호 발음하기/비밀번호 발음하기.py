import sys
input = sys.stdin.readline

def one(string) :
    for i in string :
        if i in ['a', 'e', 'i', 'o', 'u'] :
            return True
    return False

def two(string) :
    jcount = 0
    mcount = 0
    for i in string :
        if i in ['a', 'e', 'i', 'o', 'u'] :
            mcount += 1
            jcount = 0
        else :
            jcount += 1
            mcount = 0
        if mcount >= 3 or jcount >= 3 :
            return False
    return True

def three(string) :
    before = ''
    for index, i in enumerate(string) :
        if index == 0 :
            before = i
            continue
        if before == i :
            if before + i != 'ee' and before + i != 'oo' :
                return False
        before = i
    return True

while True :
    s = input().rstrip()
    if s == 'end' :
        break
    print("<", end = "")
    print(s, end = "")
    print("> is ", end = "")
    if one(s) and two(s) and three(s) :
        print("acceptable.")
    else :
        print("not acceptable.")