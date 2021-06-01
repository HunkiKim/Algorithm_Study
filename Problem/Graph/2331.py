from collections import deque
dq = deque()
A,B = map(int,input().split())
ans = 0
fans=0
flag = False


for i in str(A):
    fans += int(i)**B
if fans == A:
    print(0)
    exit(0)

dq.append(A)
while flag == False:
    for i in str(A):
       ans += int(i)**B 
    for i in dq:
        if ans == i:
            flag = True
    A=ans
    dq.append(ans)
    ans = 0
count = 0
for i in dq:
    if i==A:
        print(count)
        break
    count +=1
    
