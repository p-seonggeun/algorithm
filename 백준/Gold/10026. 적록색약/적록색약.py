import copy
import sys
sys.setrecursionlimit(1000000)

n = int(input())
l = []
rgb_l = []
for _ in range(n) :
    l.append(list(map(str, input())))
rgb_l = copy.deepcopy(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_r(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    if l[x][y] == 'R' :
        l[x][y] = 'C'
        dfs_r(x + dx[0], y + dy[0])
        dfs_r(x + dx[1], y + dy[1])
        dfs_r(x + dx[2], y + dy[2])
        dfs_r(x + dx[3], y + dy[3])
        return True
    return False

def dfs_g(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    if l[x][y] == 'G' :
        l[x][y] = 'C'
        dfs_g(x + dx[0], y + dy[0])
        dfs_g(x + dx[1], y + dy[1])
        dfs_g(x + dx[2], y + dy[2])
        dfs_g(x + dx[3], y + dy[3])
        return True
    return False

def dfs_b(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    if l[x][y] == 'B' :
        l[x][y] = 'C'
        dfs_b(x + dx[0], y + dy[0])
        dfs_b(x + dx[1], y + dy[1])
        dfs_b(x + dx[2], y + dy[2])
        dfs_b(x + dx[3], y + dy[3])
        return True
    return False

def dfs_RG(x, y) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    if rgb_l[x][y] == 'R' or rgb_l[x][y] == 'G':
        rgb_l[x][y] = 'C'
        dfs_RG(x + dx[0], y + dy[0])
        dfs_RG(x + dx[1], y + dy[1])
        dfs_RG(x + dx[2], y + dy[2])
        dfs_RG(x + dx[3], y + dy[3])
        return True
    return False
rgb_x_r = 0
rgb_x_g = 0
rgb_x_b = 0
rgb_o_rg = 0

for i in range(n) :
    for j in range(n) :
        if dfs_r(i, j) :
            rgb_x_r += 1
        if dfs_g(i, j) :
            rgb_x_g += 1
        if dfs_b(i, j) :
            rgb_x_b += 1
        if dfs_RG(i, j) :
            rgb_o_rg += 1

rgb_x = rgb_x_r + rgb_x_g + rgb_x_b
rgb_o = rgb_x_b + rgb_o_rg

print(rgb_x, rgb_o)