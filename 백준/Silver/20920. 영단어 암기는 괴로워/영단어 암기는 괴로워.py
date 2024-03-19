import sys
input = sys.stdin.readline

n, m = map(int, input().split())
word_dict = {}
for _ in range(n) :
    word = input().rstrip()
    if len(word) >= m :
        if word in word_dict :
            word_dict[word] += 1
        else :
            word_dict[word] = 1

word_list = list(word_dict.items())
word_list.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_list :
    print(i[0])
