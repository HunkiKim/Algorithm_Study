from itertools import combinations
N = int(input())
S = list()
B = list()
for i in range(N):
    tmp = list(map(int, input().split()))
    # print(tmp)
    S.append(tmp[0])
    B.append(tmp[1])
SC = list()
BC = list()
for i in range(1, N + 1):
    SC.append(list(combinations(S, i)))
for i in range(1, N + 1):
    BC.append(list(combinations(B, i)))
S = {}
B = {}
for i in SC:
    tmp = 1
    # print(i)
    for j in i:
        tmp = 1
        for k in j:
            # print(j)
            tmp = k * tmp
        if len(j) not in S:
            S[len(j)] = [tmp]
        else:
            S[len(j)].append(tmp)
        # S.append((tmp, len(j)))
for i in BC:
    tmp = 0
    # print(i)
    for j in i:
        tmp = 0
        for k in j:
            # print(j)
            tmp = k + tmp
        if len(j) not in B:
            B[len(j)] = [tmp]
        else:
            B[len(j)].append(tmp)
        # B.append((tmp,len(j)))
ans = 1000000000000000
for i in range(1, N + 1):
    for j in range(len(S[i])):
        ans = min(ans, abs(S[i][j] - B[i][j]))

# print(S, B)
print(ans)