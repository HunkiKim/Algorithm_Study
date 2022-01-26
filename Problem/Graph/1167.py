from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def dfs(node,weight):
    global ans,ans_node
    # print("s")
    if V[node]==1:
        return
    V[node] = 1
    for i in D[node]:
        # print(visit,i[0],i)
        if V[i[0]] == 0:
            if ans < weight+i[1]:
                ans_node = i[0]
                ans = max(ans,weight+i[1])
            dfs(i[0],weight+i[1])
            # print(ans)
            


D = defaultdict(list)
N = int(input())
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    for j in range(1,len(tmp)-1,2):
        D[tmp[0]].append((tmp[j],tmp[j+1]))
ans = 0
ans_node = -1
V = [0 for _ in range(N+1)]
dfs(1,0)
ans = 0
V = [0 for _ in range(N+1)]
dfs(ans_node,0)
print(ans)