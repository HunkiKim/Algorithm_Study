T = int(input())
C = [0 for _ in range(13)]
ans = 0
C[1] = 1
C[2] = 2
C[3] = 4
for i in range(T):
    n = int(input())
    if n<4:
        print(C[n])
        continue
    for i in range(4,n+1):
        C[i] = C[i-1] + C[i-2]+ C[i-3]
    print(C[n])
    for j in range(4,13):
        C[j] = 0