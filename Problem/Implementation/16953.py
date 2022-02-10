A,B = map(int,input().split())
ans = 100000000000000
def dfs(num,cnt):
    global B,ans
    if num > B:
        return
    elif num==B:
        ans = min(ans,cnt)
        return
    dfs(num*2,cnt+1)
    dfs(int(str(num)+"1"),cnt+1)
dfs(A,1)  
if ans==100000000000000:
    print("-1")
else:
    print(ans)