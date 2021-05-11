A = int(input())
L = list(map(int, input().split()))
B = [0 for _ in range(A)]
B[0] = 1
for i in range(A):
    B[i] = 1
    for j in range(i):
        if L[i] > L[j]:
            B[i] = max(B[j]+1,B[i])

print(B)