N = int(input())
L = [list(map(int, input())) for _ in range(N)]
s = ''


def merge(x, y, n):
    f = L[y][x]
    LL = []
    nn = n // 2
    if n <= 1:
        return str(f)
    for i in range(y, y + n):
        for j in range(x, x + n):
            if L[i][j] != f:
                LL.append('(')
                LL.extend(merge(x, y, nn))
                LL.extend(merge(x + nn, y, nn))
                LL.extend(merge(x, y + nn, nn))
                LL.extend(merge(x + nn, y + nn, nn))
                LL.append(')')
                return

    return str(f)


print(''.join(merge(0, 0, N)))
