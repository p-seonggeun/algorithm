s = {'C+', 'C0', 'C-', 'B+', 'B0', 'B-', 'A+', 'A0', 'A-'}
t = {'A': 'A0', 'B': 'B0', 'C': 'C0'}

N = int(input())
S = input().rstrip()
l = []

temp = ""
for index, i in enumerate(S):
    if index == len(S) - 1 and i in ['A', 'B', 'C']:
        l.append(t[i])
        break
    if temp == "" and i in ["+", "-", "0"]:
        continue
    temp += i
    if temp in s:
        l.append(temp)
        temp = ""
    elif S[index + 1] not in ["+", "-", "0"] and temp in t:
        temp = t[temp]
        l.append(temp)
        temp = ""

answer = []
for i in range(len(l)):
    if l[i] in ['C+', 'C0', 'C-']:
        answer.append('B')
    if l[i] in ['B0', 'B-']:
        if i == 0 or l[i - 1] in ['C+', 'C0', 'C-']:
            answer.append('D')
        elif l[i - 1] in ['A+', 'A0', 'A-', 'B+', 'B0', 'B-']:
            answer.append('B')
    if l[i] in ['A-', 'B+']:
        if i == 0 or l[i - 1] in ['B0', 'B-', 'C+', 'C0', 'C-']:
            answer.append('P')
        elif l[i - 1] in ['A+', 'A0', 'A-', 'B+']:
            answer.append('D')
    if l[i] == 'A0':
        if i == 0 or l[i - 1] in ['A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']:
            answer.append('E')
        elif l[i - 1] in ['A+', 'A0']:
            answer.append('P')
    if l[i] == 'A+':
        answer.append('E')

print(''.join(answer))
