N = int(input())
def fs(n, depth, mini) :
    root = int(n ** 0.5)

    if root ** 2 == n :
        return depth

    for i in range(root, (root // (5 - depth)), -1) : 
        x = fs(n - i ** 2, depth + 1, mini)
        if mini > x :
            mini = x
    return mini

print(fs(N, 1, 5))