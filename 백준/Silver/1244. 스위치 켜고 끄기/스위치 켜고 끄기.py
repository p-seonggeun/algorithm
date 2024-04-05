import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
L = int(input())
student = []

for _ in range(L) :
    student.append(list(map(int, input().split())))

def man(index) :
    for i in range(len(S)) :
        if i % index == (index - 1) :
            if S[i] == 1 :
                S[i] = 0
            else :
                S[i] = 1

def girl(index) :
    index -= 1
    if index == 0 or index == N - 1 :
        if S[index] == 0 :
            S[index] = 1
        else :
            S[index] = 0
        return
    else :
        s, e = index, index
        while S[s] == S[e] and 0 <= s and e < N :
            s -= 1
            e += 1
            if s < 0 or e >= N :
                break
        s += 1
        e -= 1
        for i in range(s, e + 1) :
            if S[i] == 0 :
                S[i] = 1
            else :
                S[i] = 0
        return
    
def who(l) :
    for i in l :
        if i[0] == 1 :
            man(i[1])
        else :
            girl(i[1])

who(student)
S = [0] + S
for i in range(1, len(S)) :
    print(S[i], end = " ")
    if i % 20 == 0 :
        print()