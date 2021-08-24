from collections import deque

N = int(input())
L = list(map(int, input().split()))
M = int(input())
S = list(map(int, input().split()))
S.sort(reverse=True)
dq = deque(S)
L.sort(reverse=True)
if S[0] > L[0]:
    print('-1')
    exit(0)
cnt = 0
while dq:
    for i in range(len(L)):
        if len(dq) == 0:
            break
        if L[i] >= dq[0]:
            dq.popleft()
        else:
            for j in range(len(dq)):
                if L[i] >= dq[j]:
                    dq.remove(dq[j])
                    break
                else:
                    if L[i] < dq[-1]:
                        break
    cnt += 1
print(cnt)