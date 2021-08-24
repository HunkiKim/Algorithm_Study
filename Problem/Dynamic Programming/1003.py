n = int(input())
L = list()
for i in range(n):
    L.append(int(input()))


def fibo(ans):
    A = list(0 for _ in range(ans + 1))
    B = list(0 for _ in range(ans + 1))
    if ans == 0:
        print('1 0')
        return -1
    elif ans == 1:
        print('0 1')
        return -1
    A[0] = 1
    B[1] = 1
    for i in range(2, ans + 1):
        A[i] = A[i - 1] + A[i - 2]
        B[i] = B[i - 1] + B[i - 2]
    print(A[i], B[i])
    return -1


for i in L:
    fibo(i)