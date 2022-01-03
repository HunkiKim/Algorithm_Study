from collections import deque

dq = deque()
S = input()
a = list()

ans = 1
ansdq = deque()
realans = 0
cnt = 0
for i in S:
    t = 0
    if i == '(' or i == '[':
        dq.append(i)
    elif i == ')':
        t = 0
        if cnt == 0:
            print(0)
            exit(0)
        while len(dq) != 0:
            dp = dq.pop()
            if dp == '(':
                if t == 0:
                    dq.append(2)
                else:
                    dq.append(t * 2)
                break
            elif dp == '[':
                print(0)
                exit(0)
            else:
                t = t + int(dp)
    elif i == ']':
        t = 0
        if cnt == 0:
            print(0)
            exit(0)
        while len(dq) != 0:
            dp = dq.pop()
            if dp == '[':
                if t == 0:
                    dq.append(3)
                else:
                    dq.append(t * 3)
                break
            elif dp == '(':
                print(0)
                exit(0)
            else:
                t = t + int(dp)
    cnt += 1
realans = 0
# print(dq)
for i in dq:
    if i == '(' or i == '[' or i == ']' or i == ')':
        print(0)
        exit(0)
    else:
        realans += i

print(realans)