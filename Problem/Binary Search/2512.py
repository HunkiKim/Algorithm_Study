N = int(input())
L = list(map(int, input().split()))
lim = int(input())
L.sort()
count = 1
A = list()
l = 1
if sum(L) <= lim:
    print(max(L))
    exit(0)


def binary(f, e, n, ans):
    if f >= e:
        return -1
    m = (f + e) // 2
    cnt = 1
    hap = ans - m
    A = L[-1] - m  #상한선
    for i in range(len(L) - 1):
        if L[i] > A:
            hap -= (L[i] - A)
            cnt += 1
    if n - cnt < hap <= n:
        global l
        global count
        l = m
        return -1
    if n > hap:
        binary(f, m, n, ans)
    else:
        binary(m + 1, e, n, ans)


binary(1, sum(L) - lim, lim, sum(L))
print(L[-1] - l)
