import sys

n = int(input())
num = 3
slen = []
slen.append(3)
while (n > 3):
    k = 0
    while (n > slen[k]):
        k += 1
        slen.insert(k, num * 2 + n + 3)
    if n <= slen[k - 1] + k + 3:
        if n - slen[k - 1] == 1:
            n = 1
            break
        else:
            n = 2
            break
    else:
        n = n - slen[k - 1] - k - 3
if n == 1:
    print('m')
else:
    print('o')