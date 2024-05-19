import sys
input = sys.stdin.readline

answer = 0

# 첫번째부터 두번째 도시까지는 필요한 기름 넣어야하고
# 두번째 도시부터는 나보다 작은 지점을 찾아야함
# 나보다 작은 지점이 나올때까지 거리를 더하고
# 나보다 작은 지점이 나오면 거기로 점프
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
me = 0
while me != N - 1 :
    if me == N - 1 :
        break

    for i in range(me + 1, N) :
        if price[me] > price[i] :
            answer += (sum(distance[me : i]) * price[me])
            me = i
            break
    else :
        answer += (sum(distance[me : N]) * price[me])
        me = i

print(answer)