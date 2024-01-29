string = input()
count = 0
s = set()

for i in range(1, len(string) + 1) :
    for j in range(len(string)) :
        if i == 1 :
            s.add(string[j])
        else :
            s.add(string[j : j + i])

print(len(s))