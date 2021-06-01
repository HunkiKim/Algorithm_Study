K,N = map(int, input().split())
L = []
for i in range(K):
    L.append(int(input()))
F,E = 1,max(L)

if L.count(L[0]) == N:
    print(E)
    exit(0)
while True:
    if F>=E:
        if V<N:
            print(mid-1)
            break
        print(mid)
        break
    mid = (F+E)>>1
    V=sum([i // mid for i in L])
    if V>=N:
        F = mid + 1
    elif V<N:
        E = mid
    
    

