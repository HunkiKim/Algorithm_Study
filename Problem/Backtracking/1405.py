import itertools
def dfs(cnt,st):
    global n,E,W,S,N
    if cnt==n:
        f = st[0]
        e = ''
        if f == 'E' or f == 'W':
            for i in range(1,len(st)):
                if st[i]== 'N' or st[i] == 'S':
                    e = st[i]
                    break
        elif f == 'S' or f == 'N':
            for i in range(1,len(st)):
                if st[i]== 'E' or st[i] == 'W':
                    e = st[i]
                    break
        fc = 1
        ec = 0
        flag = False
        fflag = False
        if f == 'E' and e == 'N':
            
            for i in range(1,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'W':
                    fc -=1
                elif st[i] == 'S':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'E' and e == 'S':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'W':
                    fc -=1
                elif st[i] == 'N':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'E' and e == '':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i] == 'W':
                    fc -=1
                if fc == 0:
                    flag = True
                    break
        elif f == 'W' and e == 'N':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'E':
                    fc -=1
                elif st[i] == 'S':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'W' and e == 'S':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'E':
                    fc -=1
                elif st[i] == 'N':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'W' and e == '':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i] == 'E':
                    fc -=1
                if fc == 0:
                    flag = True
                    break
        elif f == 'N' and e == 'W':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'S':
                    fc -=1
                elif st[i] == 'E':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'N' and e == 'E':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'S':
                    fc -=1
                elif st[i] == 'W':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'N' and e == '':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i] == 'S':
                    fc -=1      
                if fc == 0 :
                    flag = True
                    break 
        elif f == 'S' and e == 'E':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'N':
                    fc -=1
                elif st[i] == 'W':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'S' and e == 'W':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i]==e:
                    ec += 1
                    fflag = True
                elif st[i] == 'N':
                    fc -=1
                elif st[i] == 'E':
                    ec -= 1
                if (fc == 0 or ec == 0) and fflag == True:
                    flag = True
                    break
        elif f == 'S' and e == '':
            for i in range(0,len(st)):
                if f == st[i]:
                    fc += 1
                elif st[i] == 'N':
                    fc -=1 
                if fc == 0 :
                    flag = True
                    break
        if flag==False and st not in AL:
            AL.append(st)
            return
    else:
        if E>0:
            st += 'E'
            if st not in D:
                dfs(cnt+1,st)
            st = st[:len(st)-1]
        if W>0:
            st += 'W'
            if st not in D:
                dfs(cnt+1,st)
            st = st[:len(st)-1]
        if N>0:
            st += 'N'
            if st not in D:
                dfs(cnt+1,st)
            st = st[:len(st)-1]
        if S>0:
            st += 'S'
            if st not in D:
                dfs(cnt+1,st)
            st = st[:len(st)-1]
AL = list()
D = {}

L = list(map(int,input().split()))
n = L[0]
E = L[1]/100
W = L[2]/100
S = L[3]/100
N = L[4]/100
# V = [[0 for _ in range(n*2)] for _ in range(n*2)]
print(n,E,W,S,N)
dfs(0,'')
EWSN = list()
if E>0:
    EWSN.append('E')
if W>0:
    EWSN.append('W')
if S>0:
    EWSN.append('S')
if N>0:
    EWSN.append('N')
ec = 1
for i in range(n):
    ec *= len(EWSN)
print(ec,AL)
print(round((len(AL)/ec),9))
