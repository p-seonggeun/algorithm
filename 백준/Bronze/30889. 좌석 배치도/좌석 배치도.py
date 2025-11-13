N = int(input())
l = [['.'] * 20 for _ in range(10)]

for _ in range(N):
    temp = input().rstrip()
    r = ord(temp[0]) - 65
    c = int(temp[1:]) - 1

    l[r][c] = 'o'


for i in l:
    for j in i:
        print(j, end='')
    print()