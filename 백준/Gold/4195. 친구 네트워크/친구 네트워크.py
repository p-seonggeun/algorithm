import sys
input = sys.stdin.readline

n = int(input())
def find(name) :
    if network[name] != name :
        network[name] = find(network[name])
    return network[name]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a < b :
        network[b] = a
        cnt[a] += cnt[b]
        cnt[b] = 0
    
    elif a > b :
        network[a] = b
        cnt[b] += cnt[a]
        cnt[a] = 0
    
for _ in range(n) :
    F = int(input())
    cnt = {}
    network = {}
    for _ in range(F) :
        s1, s2 = input().rstrip().split()
        if network.get(s1) == None :
            network[s1] = s1
            cnt[s1] = 1
        if network.get(s2) == None :
            network[s2] = s2
            cnt[s2] = 1
        union(s1, s2)
        print(cnt[find(s1)])