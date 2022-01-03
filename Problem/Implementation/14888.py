from itertools import combinations
from itertools import permutations

minans = 100000000000
maxans = -100000000000
N = int(input())
L = list(map(int, input().split()))
O = list(map(int, input().split()))
Oper = list()
for i in range(O[0]):
    Oper.append("+")
for i in range(O[1]):
    Oper.append("-")
for i in range(O[2]):
    Oper.append("*")
for i in range(O[3]):
    Oper.append("/")
OP = list(permutations(Oper, N - 1))
D = {}
for i in OP:
    D[i] = 1
for i in D:
    ans = L[0]
    cnt = 1
    for j in i:
        if j == '+':
            ans += L[cnt]
        elif j == '-':
            ans -= L[cnt]
        elif j == '*':
            ans *= L[cnt]
        elif j == '/':
            nans = 0
            if ans < 0:
                nans = (abs(ans)) // L[cnt]
                ans = -nans
            elif L[cnt] < 0:
                nans = ans // abs(L[cnt])
                ans = -nans
            else:
                ans = ans // L[cnt]
        cnt += 1
    minans = min(minans, ans)
    maxans = max(maxans, ans)
print(maxans)
print(minans)
