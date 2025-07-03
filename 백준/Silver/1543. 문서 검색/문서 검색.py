note = input().rstrip()
word = input().rstrip()

index = 0
answer = 0
while index <= len(note) - len(word):
    if note[index:index+len(word)] == word:
        index += len(word)
        answer +=1
    else:
        index +=1

print(answer)