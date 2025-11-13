T = int(input())

for _ in range(T):
    s = int(input()) # 자동차 가격
    n = int(input()) # 해빈이가 사려는 옵션 개수
    for _ in range(n):
        q, p = map(int, input().split())

        s += q * p
    print(s)