A = int(input())
L = list(map(int, input().split()))
B = [1 for _ in range(A)]
B[0] = 1
for i in range(1,A):
    for j in range(i):
        if L[i] < L[j]:
            B[i] = max(B[j] + 1,B[i])
            
        
print(B)