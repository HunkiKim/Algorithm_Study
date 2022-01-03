from collections import deque
N =int(input())
In = list(map(int,input().split()))
Po = list(map(int,input().split()))
root = Po[-1]
root2 = Po[-1]
root = In.index(root)
# print(root)
L = deque(In[:root])
R = deque(In[root+1:len(In)])
cnt = 0
Ans = deque()
while True:
    if len(R)==0:
        break
    elif len(R)==1:
        Ans.appendleft(R.pop())
    elif len(R)==2:
        Ans.appendleft(R.pop())
        Ans.appendleft(R.pop())
    else:
        Ans.appendleft(R[-3])
        Ans.appendleft(R[-1])
        Ans.appendleft(R[-2])
        R.pop()
        R.pop()
        R.pop()
while True:
    if len(L)==0:
        break
    elif len(L)==1:
        Ans.appendleft(L.pop())
    elif len(L)==2:
        Ans.appendleft(L.popleft())
        Ans.appendleft(L.popleft())
    else:
        Ans.appendleft(L[2])
        Ans.appendleft(L[0])
        Ans.appendleft(L[1])
        L.popleft()
        L.popleft()
        L.popleft()


# print(L,R,)


Ans.appendleft(root2)
answer =list()
for i in range(len(Ans)):
    print(Ans[i], end=' ')