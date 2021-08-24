from collections import deque

N = int(input())
L = list(map(int, input().split()))
a, b = map(int, input().split())
V = [0] * N
dq = deque()
cnt = 0
ans = 0
dq.append(a)
while True:
    s = len(dq)
    flag = False
    cnt += 1
    for i in range(s):
        p = dq.pop()
        V[p] = 1
        if abs(b - p) % L[i] == 0:
            flag = True
            break
        else:
            V[p] = 1
            if b>p:
                q.append(n) = L[i] + 1
    if flag == True:
        break
print(cnt)
