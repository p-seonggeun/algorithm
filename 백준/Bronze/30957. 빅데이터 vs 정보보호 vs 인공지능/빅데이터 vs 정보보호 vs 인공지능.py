N = int(input())
l = list(input())

d = {'B':0,'S':0,'A':0}

for i in l:
    d[i] += 1

m = max(d.values())

answer = ""
for i in d:
    if d[i] == m:
        answer += i

if answer == "BSA":
    print("SCU")
else:
    print(answer)