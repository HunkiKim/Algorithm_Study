T = int(input())
for i in range(T):
    L = list()
    N = int(input())
    cnt = 1
    for j in range(N):
        a, b = map(int, input().split())
        L.append((a, b))
    L.sort()
    Max = L[0][1]
    for j in range(0, N - 1):
        if Max > L[j + 1][1]:
            cnt += 1
            Max = L[j + 1][1]
            if Max == 1:
                break

    print(cnt)