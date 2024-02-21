import sys
input = sys.stdin.readline

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1) :
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])] :
            return False
    return answer

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(n) :
        l.append(str(input()).rstrip())
    if (solution(l)) :
        print("YES")
    else :
        print("NO")