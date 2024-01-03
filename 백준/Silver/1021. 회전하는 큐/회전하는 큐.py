from collections import deque

n, m = map(int, input().split())
num_list = deque([i for i in range(1, n + 1)])
l = list(map(int, input().split()))
count = 0

for i in l :
    if num_list.index(i) == 0 :
        num_list.popleft()
    else :
        while (num_list.index(i) != 0) :
            if len(num_list) % 2 != 0 :
                if num_list.index(i) > (len(num_list) // 2) :
                    num_list.rotate(1)
                else :
                    num_list.rotate(-1)
            else :
                if num_list.index(i) >= (len(num_list) // 2) :
                    num_list.rotate(1)
                else :
                    num_list.rotate(-1)
            count += 1
        num_list.popleft()

print(count)