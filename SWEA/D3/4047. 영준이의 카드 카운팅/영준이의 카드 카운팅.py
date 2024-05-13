#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1) :
    s = input().rstrip()
    card = []
    for i in range(0, len(s), 3) :
        card.append(s[i : i + 3])
    number = {"S" : 13, "D" : 13, "H" : 13, "C" : 13}
    if len(set(card)) != len(card) :
        print(f"#{tc}", "ERROR")
        continue
    else :
        for i in card :
            number[i[0]] -= 1
        print(f"#{tc}", *list(number.values()))
