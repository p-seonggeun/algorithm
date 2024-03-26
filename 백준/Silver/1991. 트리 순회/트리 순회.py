import sys
input = sys.stdin.readline

N = int(input())
graph = {}

def preOrder(n) :
    if n == '.' :
        return
    print(n, end = "")
    for i in graph[n] :
        preOrder(i)

def inOrder(n) :
    if n == '.' :
        return
    a, b = graph[n]
    inOrder(a)
    print(n, end = "")
    inOrder(b)

def postOrder(n) :
    if n == '.' :
        return
    a, b = graph[n]
    postOrder(a)
    postOrder(b)
    print(n, end = "")

for _ in range(N) :
    a, b, c = input().rstrip().split(" ")
    graph[a] = [b, c]

preOrder("A")
print()
inOrder("A")
print()
postOrder("A")