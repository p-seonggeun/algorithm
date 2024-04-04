import sys
input = sys.stdin.readline

N, G = input().rstrip().split()
p = set()
for _ in range(int(N)) :
    p.add(input().rstrip())

game = {'Y' : 2, 'F' : 3, 'O' : 4}

print(len(p) // (game[G] - 1))