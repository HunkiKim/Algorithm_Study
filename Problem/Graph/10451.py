from collections import deque
dq = deque()
N = int(input())
C = 0
L = []
for i in range(N):
    S = input()
    dq.append(0)
    A = input().split()
    for j in A:
        dq.append(int(j))
    for j in range(1,len(dq)):
        count = j
        if count in L:
            continue
        else:
            while True:
                if count in L:
                    C += 1
                    break
                else:
                    L.append(count)
                    count = dq[count]
    print(C)
    C=0
    dq.clear()
    L.clear()
    A.clear()