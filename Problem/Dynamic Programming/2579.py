# 계단은 1 or 2
A = int(input())
L = []
ANS = [0 for _ in range(A)]
C = [0 for _ in range(A)]

for i in range(A):
    L.append(int(input()))

if A==1:
    print(L[0])
    exit(0)
elif A==2:
    print(L[0]+L[1])
    exit(0)
# 리스트 생성
ANS[0] = L[0] # 초기 0 
C[0] = 1
for i in range(1,A-1):
    if C[i-1] == 0:
        C[i] = 1
        ANS[i] = ANS[i-1] + L[i]
    elif C[i-1]<2:
        C[i] =C[i-1] +  1
        ANS[i] = ANS[i-1] + L[i]
    else:
        if ANS[i-1]>ANS[i-1] + L[i] - L[i-2] and ANS[i-1]>ANS[i-2] + L[i]:
            ANS[i] = ANS[i-1]
            C[i] = 0
        elif ANS[i-2] + L[i] > ANS[i-1]:
            C[i] = 1
            ANS[i] = ANS[i-2] + L[i]
        else:
            C[i] = C[i-1] + 1
            ANS[i] = ANS[i-1] + L[i] - L[i-2]

i += 1
if C[i-1] == 2:
    if ANS[i-2] + L[i] >= ANS[i-1] + L[i] - L[i-2]:
        ANS[i] = ANS[i-2] + L[i]
    else:
        ANS[i] = ANS[i-1] + L[i] - L[i-2]
       
else:
    ANS[i] = ANS[i-1] + L[i]

print(ANS[i]) 



