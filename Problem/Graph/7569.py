M, N, H = map(int, input().split())
NH = N * H
L = [[0] * M for _ in range(NH)]
V = [[0] * M for _ in range(NH)]
print(L)
for i in range(NH):
    A = input().split()
    for j in range(len(A)):
        L[i][j] = A[j]
if not '0' in L:
    print('0')
    exit(0)
cnt = 0
flag = False
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    for i in range(M):
        for j in range(NH):


print(L)