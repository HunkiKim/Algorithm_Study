import sys
from itertools import combinations
from itertools import permutations
# def recur():

input = sys.stdin.readline
N = int(input())
L = list()
LL = list()
for i in range(N):
    LL.append(i+1)
    L.append(list(map(int,input().split())))
D = {}
C = list(combinations(LL,N//2))
mnum = 100000000000000000
for i in C:
    LLL = list()
    for j in range(1,N+1):
        if i.count(j)==0:
            LLL.append(j)
    D[i] = LLL

for i in D:
    P = list(permutations(i,2))
    P2 = list(permutations(D[i],2))
    a1 = 0
    a2 = 0
    for j in P:
        a1 += L[j[0]-1][j[1]-1]
    for j in P2:
        a2 += L[j[0]-1][j[1]-1]
    mnum = min(mnum,abs(a1-a2))
print(mnum)