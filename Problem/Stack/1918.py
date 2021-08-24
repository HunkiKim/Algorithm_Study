from collections import deque

dq = deque()
A = input()
ans = ""
for i in A:
    if i.isalpha():
        ans += i
    else:
        if i == '(':
            dq.append(i)
        elif i == '*' or i == '/':
            while dq and (dq[-1] == "*" or dq[-1] == "/"):
                ans += dq.pop()
            dq.append(i)
        elif i == '+' or i == '-':
            while dq and (dq[-1] == '+' or dq[-1] == '-' or dq[-1] == '/'
                          or dq[-1] == '*'):
                ans += dq.pop()
            dq.append(i)
        elif i == ")":
            while dq and dq[-1] != "(":
                ans += dq.pop()
            dq.pop()
while dq:
    ans += dq.pop()
print(ans)