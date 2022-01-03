from itertools import permutations
from itertools import combinations
N = int(input())
L = list()
S = {}
B = {}

for _ in range(N):
    LL = list(map(int,input().split()))
    LL[0] = str(LL[0])
    L.append(LL)
print(L)
flag = True
ans = list()
for i in range(len(L)):
    
    if L[i][1]==3:
        print(1)
        exit(0)
    elif L[i][1]==2:
        s1 = (L[i][0][0],0)
        s2 = (L[i][0][1],1)
        s3 = (L[i][0][2],2)
        for j in range(len(L)):
            if i==j:
                continue
            if L[j][1]==1 and (L[j][0].count(s1[0])>0 or L[j][0].count(s2[0]>0 or L[j][0].count(s3[0])>0)):
                continue
            else:
                if L[j][0].count(s1[0])==0:
                    ans=L[j][0][0] + s2[0] + s3[0]
                elif L[j][0].count(s2[0])==0:
                    ans = s1[0] + L[j][0][1] + s3[0]
                else:
                    ans = s1[0] + s2[0] + L[j][0][2]
                break
            if L[j][2]==1 and (L[j][0].count(s1[0])==0 and L[j][0].count(s2[0]==0 and L[j][0].count(s3[0])==0)):
                
        print(nlist)
    
    
    
    