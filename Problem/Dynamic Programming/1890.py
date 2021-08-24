n = int(input())
L = list()
D = [[-1] * n for _ in range(n)]
for i in range(n):
    A = list(map(int, input().split()))
    L.append(A)


def ref(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    if D[y][x] == -1:
        D[y][x] = 0
        if x + L[y][x] <= n - 1:
            D[y][x] += ref(x + L[y][x], y)
        if y + L[y][x] <= n - 1:
            D[y][x] += ref(x, y + L[y][x])
    return D[y][x]


a = ref(0, 0)
print(a)