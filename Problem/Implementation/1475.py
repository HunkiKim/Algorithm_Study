N = input()
D = {}
for i in range(10):
    D[i] = 0

for i in N:
    n = int(i)
    if n == 6 or n == 9:
        if D[6] == D[9]:
            D[6] += 1
        elif D[6] > D[9]:
            D[9] += 1
        else:
            D[6] += 1
    else:
        D[n] += 1
ans = 0
for i in D:
    ans = max(D[i],ans)
print(ans)