x, y = map(int, input().split())
days = {0 : 'SUN', 1 : 'MON', 2 : 'TUE', 3 : 'WED', 4 : 'THU', 5 : 'FRI', 6 : 'SAT'}
day = 0
to = [1, 3, 5, 7, 8, 10, 12]
t = [4, 6, 9, 11]
for i in range(1, x) :
    if i in to :
        day += 31
    elif i in t :
        day += 30
    else :
        day += 28

day += y
print(days[day % 7])