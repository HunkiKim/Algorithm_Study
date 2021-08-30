def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    num = 0
    while t * (m + 1) >= len(answer):
        a = ''
        if n != 10:
            a = str(convert(num, n))
        else:
            a = str(num)
        num += 1
        answer += a
    ans = ''
    num = p - 1
    while t != len(ans):
        ans += answer[num].upper()
        num += m
    print(ans)
    return ans