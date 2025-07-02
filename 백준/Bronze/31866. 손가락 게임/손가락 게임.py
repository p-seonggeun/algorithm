A, B = map(int, input().split())

d = {0: '바위', 2: '가위', 5: '보'}
result = {'바위가위': '>',
          '가위보': '>',
          '보바위': '>',
          '가위바위': '<',
          '보가위': '<',
          '바위보': '<'}
if A in d:
    A = d[A]
else:
    A = '무효'

if B in d:
    B = d[B]
else:
    B = '무효'

if A == B:
    print("=")
elif A != '무효' and B == '무효':
    print(">")
elif A == '무효' and B != '무효':
    print("<")
else:
    print(result[A + B])
