N,T,P = map(int,input().split())
if N==0 and P>=1:
    print(1)
    exit(0)
L = list(map(int,input().split()))
L.append(T)

L.sort(reverse=True)
if len(L) > P:
    lp = L.pop()
    if lp == T:
        print(-1)
        exit(0)
cnt = 1
D = {}
tmp = 1
for i in range(len(L)):
    if i+1<len(L) and L[i] != L[i+1]:
        D[L[i]] = cnt
        cnt += tmp
        tmp = 1
    else:
        tmp+=1
if L[i] not in D:
    D[L[i]] = cnt

if T not in D:
    print(-1)
elif D[T] > P:
    print(-1)
else:
    print(D[T])
