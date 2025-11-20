n, k = map(int, input().split())

def change(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)
        result.append(r)
    return ''.join(map(str, result[::-1]))

a = change(n, k)
a = a.split("0")
a = [i for i in a if i != '']
b = sum(map(int, a))
answer = change(b, k)
print(answer)