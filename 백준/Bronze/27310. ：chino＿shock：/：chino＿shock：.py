emoji = input().rstrip()
print(len(emoji) + emoji.count(':') + emoji.count('_') * 5)