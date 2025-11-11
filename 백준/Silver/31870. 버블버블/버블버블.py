N = int(input())
A = list(map(int, input().split()))

# 삽입 정렬
def a(A):
    A = A[:]
    result = 0
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                result += 1
            else:
                break
    return result

def b(A):
    A = A[::-1]
    result = 1
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                result += 1
            else:
                break
    return result

print(min(a(A), b(A)))