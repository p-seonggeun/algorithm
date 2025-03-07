s1 = input()
s2 = input()

l1 = [0] * 26
l2 = [0] * 26

for i in s1 :
    l1[ord(i) - 97] += 1

for i in s2 :
    l2[ord(i) - 97] += 1

answer = 0
for i in range(26) :
    if l1[i] != l2[i] :
        answer += max(l1[i], l2[i]) - min(l1[i], l2[i])
print(answer)