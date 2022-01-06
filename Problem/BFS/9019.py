from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
ans = ''
for i in range(T):
    dq = deque()
    V = [0 for _ in range(10000)]
    a,b = map(int,input().split())
    # print(a,b)

    dq.append(('',a))
    V[a] = 1
    while dq:
        p = dq.popleft()
        alpha,num= p[0],p[1]
        if num==b:
            ans = alpha
            break
        ns = 0
        if num==0:
            ns = 9999
        else:
            ns = num-1
        nd = (2*num % 10000)
        nl = (num%1000)*10 + num//1000
        nr = (num%10)*1000 + num // 10
        if V[nd] == 0:
            dq.append((alpha+'D',nd))
            V[nd] = 1
        if V[ns] == 0:    
            dq.append((alpha+'S',ns))
            V[ns] = 1
        if V[nl] == 0:
            V[nl] = 1
            dq.append((alpha+'L',nl))
        if V[nr] == 0:
            V[nr] = 1
            dq.append((alpha+'R',nr))
    print(ans)
        

    