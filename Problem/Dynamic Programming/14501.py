from collections import deque
dq = deque()
N = int(input())
A = [0 for _ in range(N+1)]
for i in range(N):
    t,pp = map(int,input().split())
    dq.append((t,pp,i))
    A[i] = A[i-1]
    for j in range(len(dq)):        
        p = dq.popleft()
        if i-p[0]-p[2]+1 == 0:
            A[i] = max(A[i],A[i-p[0]] + p[1])
        else:
            dq.append(p)
        if len(dq)==0:
            break
    # print(A)
print(max(A))

