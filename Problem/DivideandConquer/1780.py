N = int(input())
L = list()
for i in range(N):
    A = list(map(int, input().split()))
    L.append(A)
Dic = {}
Dic[0], Dic[1], Dic[-1] = 0, 0, 0


def fun(x, y, n):
    if n == 1:
        Dic[L[y][x]] += 1
        return
    nn = n // 3
    for i in range(y, y + n):
        for j in range(x, x + n):
            if L[y][x] != L[i][j]:
                fun(x, y, nn)
                fun(x + nn, y, nn)
                fun(x + nn * 2, y, nn)
                fun(x, y + nn, nn)
                fun(x + nn, y + nn, nn)
                fun(x + nn * 2, y + nn, nn)
                fun(x, y + nn * 2, nn)
                fun(x + nn, y + nn * 2, nn)
                fun(x + nn * 2, y + nn * 2, nn)
                return
    Dic[L[y][x]] += 1
    return -1


fun(0, 0, N)
print(Dic[-1])
print(Dic[0])
print(Dic[1])