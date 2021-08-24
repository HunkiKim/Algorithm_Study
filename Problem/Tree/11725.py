from operator import itemgetter
import sys

limit_number = 10**5
sys.setrecursionlimit(limit_number)
N = int(input())
T = [[] for _ in range(N + 1)]
L = list()
T[1] = []
for _ in range(N - 1):
    A, B = map(int, input().split())
    T[A].append(B)
    T[B].append(A)
P = [0 for _ in range(N + 1)]


def dfs(n):
    for i in T[n]:
        if P[i] == 0:
            P[i] = n
            dfs(i)


dfs(1)
for i in range(2, N + 1):
    print(P[i])
