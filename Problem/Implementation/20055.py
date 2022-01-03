from collections import deque
L1 = deque()
L2 = deque()
N,K = map(int,input().split())
l = list(map(int,input().split()))
for i in range(N):
    L1.append(l[i])
for i in range(N,N*2):
    L2.append(l[i])
cnt = 0
ccnt = 0
while cnt<K:
    print(ccnt)
    ccnt += 1
    a = L1.pop()
    b = L2.popleft()
    L2.append(a)
    b -=1
    if b>0:
        L1.appendleft(b)
    elif b==0:
        cnt += 1

print(L1,L2)
print(cnt)