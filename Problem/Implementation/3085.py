N = int(input())
L = list()
for i in range(N):
    tmp = list(input())
    L.append(tmp)
ans = 0
cnt = 1
cnt2 = 1
for i in range(N):
    for j in range(N-1):
        if j+1 < N and L[i][j] != L[i][j+1]:
            L[i][j], L[i][j+1] = L[i][j+1], L[i][j]
            # print(L)
            for k in range(N):
                cnt = 1
                cnt2 = 1
                for l in range(1,N):
                   
                    if L[k][l] == L[k][l-1]:
                        cnt += 1
                    else:
                        ans = max(cnt,ans)
                        cnt = 1
                    if L[l][k] == L[l-1][k]:
                        cnt2 += 1
                    else:
                        ans = max(cnt2,ans)
                        cnt2 = 1
                
                ans = max(cnt,cnt2,ans)
            L[i][j], L[i][j+1] = L[i][j+1], L[i][j]
        if i+1 < N and L[i+1][j] != L[i][j]:
            L[i][j], L[i+1][j] = L[i+1][j], L[i][j]
            # print(L)
            for k in range(N):
                cnt = 1
                cnt2 = 1
                for l in range(1,N):
                    if L[k][l] == L[k][l-1]:
                        cnt += 1
                    else:
                        ans = max(cnt,ans)
                        cnt = 1
                    if L[l][k] == L[l-1][k]:
                        cnt2 += 1
                    else:
                        ans = max(cnt2,ans)
                        cnt2 = 1
                ans = max(cnt,cnt2,ans)
            L[i][j], L[i+1][j] = L[i+1][j], L[i][j]
        if j-1 >= 0 and L[i][j] != L[i][j-1]:
            L[i][j], L[i][j-1] = L[i][j-1], L[i][j]
            # print(L)
            for k in range(N):
                cnt = 1
                cnt2 = 1
                for l in range(1,N):
                    
                    if L[k][l] == L[k][l-1]:
                        cnt += 1
                    else:
                        ans = max(cnt,ans)
                        cnt = 1
                    if L[l][k] == L[l-1][k]:
                        cnt2 += 1
                    else:
                        ans = max(cnt2,ans)
                        cnt2 = 1
                ans = max(cnt,cnt2,ans)
            L[i][j], L[i][j-1] = L[i][j-1], L[i][j]
        if i-1 > 0 and L[i-1][j] != L[i][j]:
            L[i][j], L[i-1][j] = L[i-1][j], L[i][j]
            # print(L)
            for k in range(N):
                cnt = 1
                cnt2 = 1
                for l in range(1,N):
                    
                    if L[k][l] == L[k][l-1]:
                        cnt += 1
                    else:
                        ans = max(cnt,ans)
                        cnt = 1
                    if L[l][k] == L[l-1][k]:
                        cnt2 += 1
                    else:
                        ans = max(cnt2,ans)
                        cnt2 = 1
                  
                ans = max(cnt,cnt2,ans)
            L[i][j], L[i-1][j] = L[i-1][j], L[i][j]
print(ans)