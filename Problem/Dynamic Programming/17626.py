import math
INF = 100000000000
N = int(input())
L = [0,1]

for i in range(2,N+1):
    m = INF
    j = 1
    while j**2<=i:
        m = min(m,L[i-j**2])
        j+=1
    L.append(m+1)
print(L[N])