import sys
import heapq
import math
from typing import ClassVar
from collections import deque

INF = 1000000
input = sys.stdin.readline


class Node:
    def __init__(self, data1, data2, weight):
        self.data = data1
        self.link = list()
        self.link.append(data2)
        self.weight = {}
        self.weight[data2] = weight


N = int(input())
if N == 1:
    print(0)
    exit(0)
L = [0 for _ in range(N + 1)]
D = {}
for i in range(N - 1):
    A, B, C = map(int, input().split())
    if not A in D:
        D[A] = Node(A, B, C)
    else:
        D[A].link.append(B)
        D[A].weight[B] = C
    if not B in D:
        D[B] = Node(B, A, C)
    else:
        D[B].link.append(A)
        D[B].weight[A] = C
# Tree 완성
# Dijkstra 만들기
sorted(D.keys())
dq = deque()
dq.append(1)
V = {}
num = 0
while dq:
    i = dq.popleft()

    if i in V:
        continue
    V[i] = 1

    for j in D[i].link:
        if j in V:
            continue
        L[j] = L[i] + D[i].weight[j]
        dq.append(j)
        if L[num] < L[j]:
            num = j
L = [0 for _ in range(N + 1)]
V = {}
dq = deque()
dq.append(num)
while dq:
    i = dq.popleft()

    if i in V:
        continue
    V[i] = 1

    for j in D[i].link:
        if j in V:
            continue
        L[j] = L[i] + D[i].weight[j]
        dq.append(j)

ans = max(L)
print(ans)
# for i in D:  # i-> target node
#     print(i)
#     for j in D[i].link:  # link node
#         if L[j] == INF:
#             L[j] = D[i].weight[j]
#         else:
#             L[j] = min(L[j], L[i] + D[i].weight[j])
