N= int(input())
L = list(map(int, input().split()))
D = {}
for i in L:
    if not i in D:
        D[i] = 1
    else:
        D[i] += 1
M = int(input())
S = list(map(int, input().split()))
F,E = 0,len(L)-1

for i in range(len(S)):
    while True:
        if F>=E:
            if not S[i] in D:
                print('0' , end = " ")
            else:
                print((D[S[i]]), end = " ")
            break
        mid = (F+E) >> 1

        if L[mid] > S[i]:
            E = mid
        elif L[mid] < S[i]:
            F = mid+1
        else:
            print(D[S[i]], end = " ")
            break
