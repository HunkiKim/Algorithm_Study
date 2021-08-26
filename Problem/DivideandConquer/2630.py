import sys

input = sys.stdin.readline


def dfs(n, x, y, a, nn):
    A = L[y][x]
    B = 0
    C = 0

    if n == 1:
        return A
    for i in range(x, x + n):
        for j in range(y, y + n):
            if L[j][i] != A:
                for k in range(a * 2):
                    for l in range(a * 2):
                        LL.append(
                            dfs(n // 2, x + k * (n // 2), y + l * (n // 2), a,
                                nn))
                return
    if n == nn:
        if A == 1:
            print(0)
            print(1)
            exit(0)
        else:
            print(1)
            print(0)
            exit(0)

    return A


LL = list()
N = int(input())
L = list()
B = 0
C = 0
for i in range(N):
    L.append(list(map(int, input().split())))
dfs(N, 0, 0, 1, N)
for i in LL:
    if i == 1:
        B += 1
    elif i == 0:
        C += 1

print(C)
print(B)
