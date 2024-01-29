n = int(input())
n_len = len(str(n))
s = 0

for i in range(1, n_len) :
    s += 9 * 10 ** (i - 1) * i

s += ((n - 10 ** (n_len - 1)) + 1) * n_len
print(s)