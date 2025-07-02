N, M = map(int, input().split())
if M <= 26:
    print("SN", str(N) + chr(64 + M))
else:
    a = (M - 27) // 26
    b = (M - 27) % 26
    print("SN", str(N) + chr(97 + a) + chr(97 + b))
