import sys
input = sys.stdin.readline
L = [True for _ in range(1000001)]
for i in range(2,1001):
    if L[i]:
        for j in range(i*2, 1000001, i):
            L[j] = False
while True:
    N = int(input())
    if N==0:
        break
    for i in range(3,N):
        if L[i] == True and L[N-i] == True:
            m = N-i
            print(N,"=",N-m,"+",m) 
            break
    