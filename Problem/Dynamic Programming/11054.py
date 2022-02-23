N = int(input())
L = list(map(int,input().split()))
A = [1 for _ in range(N)]
D = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if L[i]>L[j]:
            A[i] = max(A[j]+1,A[i]) 
        elif L[i]==L[j]:
            A[i] = A[j]
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if L[i]>L[j]:
            D[i] = max(D[j]+1, D[i])
ans = 0
# print(A,D)
if A.count(1)==N:
    ans = max(D)
elif D.count(1)==N:
    ans = max(A)
else:
    for i in range(1,N-1):
        ans = max(A[i] + D[i] -1,ans)
        
    # ans = max(D[-1]+A[i],ans)
# ans = max(ans,max(D),max(A))
print(ans)
    
