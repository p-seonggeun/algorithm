n = int(input())
first = {i * i for i in range(1, int(n ** 0.5) + 1)}
second = {x + y for x in first for y in first}
third = {x + y for x in first for y in second}

if n in first:
    print(1)
elif n in second:
    print(2)
elif n in third:
    print(3)
else:
    print(4)
