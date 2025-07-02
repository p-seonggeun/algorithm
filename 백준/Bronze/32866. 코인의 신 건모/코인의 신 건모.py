N = int(input())
X = int(input())

print("%.6f" % ((N / (N - (N * X * 0.01)) - 1) * 100))