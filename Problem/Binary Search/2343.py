import sys
N,M = map(int,input().split())
L = list(map(int,input().split()))
f,e = max(L),sum(L)
ans = sys.maxsize
cnt = 0
while True:
    # print('s')
    if f>e:
        break

    fe = (f+e)//2
    # print(fe)/
    # print(fe , f, e,ans)
    tmp = 0
    cnt = 0
    L2 = list()
    print(fe,f,e)
    for i in range(N):
        # print('안', ans,tmp,cnt)
        if tmp+L[i] > fe:
            L2.append(tmp)       
            # ans = max(tmp,ans)
            # print(tmp,fe)
            tmp = 0
            cnt += 1
            
        # print(ans,tmp,f,e,fe,cnt)
        tmp += L[i]
    # print('바',cnt,fe)
    if tmp:
        cnt += 1
    # print('바2',cnt,f,e)
    if cnt > M:
        f = fe + 1
    elif cnt == M:
        ans = min(ans,fe)
        e = fe - 1
    else:
        e = fe - 1
    
print(ans)
