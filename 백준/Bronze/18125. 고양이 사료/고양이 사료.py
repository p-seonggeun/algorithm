R, C = map(int, input().split())
first = []
for _ in range(C):
    first.append(list(map(int, input().split())))

second = []
for _ in range(R):
    second.append(list(map(int, input().split())))

result = []

for i in range(R):
    temp = []
    for j in range(C - 1, -1, -1):
        temp.append(first[j][i])
    result.append(temp)

if result != second:
    print("|>___/|     /}")
    print("| O O |    / }")
    print("( =0= )\"\"\"\"  \\")
    print("| ^  ____    |")
    print("|_|_/    ||__|")
else:
    print("|>___/|        /}")
    print("| O < |       / }")
    print("(==0==)------/ }")
    print("| ^  _____    |")
    print("|_|_/     ||__|")