from collections import deque

N = int(input())
L = list(map(int, input().split()))
M = int(input())
S = list(map(int, input().split()))
V = [0 for _ in range(M)]
S.sort(reverse=True)
L.sort(reverse=True)
cnt = 0
if S[0] > L[0]:
    print('-1')
    exit(0)
count = 0
while True:
    if V[-1] == 1:
        break
    for i in range(len(L)):
        if V[-1] == 1:
            break
        else:
            for j in range(len(S)):
                if L[i] >= S[j] and V[j] == 0:
                    V[j] = 1
                    break
    cnt += 1

print(cnt)