from collections import deque

N = input()
S = input()
dq = deque(N)
ans = list()
tmp = ''
leng = len(S)
l = S[-1]
ff = ['1','2','3','4','5','6']
# print(ff[-100:])
for i in N:
    ans.append(i)
    if i==l and ''.join(ans[-leng:])==S:
        del ans[-leng:]
    # break
if ans:
    print(''.join(ans))
else:
    print("FRULA")
# print(dq)
    

    
