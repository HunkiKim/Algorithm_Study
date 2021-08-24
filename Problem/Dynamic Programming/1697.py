from collections import deque

dq = deque()
Dic = {}
a, b = map(int, input().split())
cnt = 1
cnt2 = 1
if a == b:
    print('0')
    exit(0)
dq.append(a)
while True:
    flag = False
    s = len(dq)
    for i in range(s):
        n = dq.popleft()
        if n - 1 == b or n + 1 == b or n * 2 == b:
            flag = True
            break
        else:
            if n in Dic.keys():
                continue
            if n - 1 < 0:
                dq.append(n * 2)
                dq.append(n + 1)
            elif n * 2 > b + 20:
                dq.append(n + 1)
                dq.append(n - 1)
            else:
                dq.append(n * 2)
                dq.append(n + 1)
                dq.append(n - 1)
        Dic[n] = 1
    if flag == True:
        break
    else:
        cnt2 += 1
print(cnt2)