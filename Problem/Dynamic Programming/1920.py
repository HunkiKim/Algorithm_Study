N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
F,E = min(A),max(A)
FF = F
EE = E
A.sort()
for i in B:
    while True:
        if FF > EE:
            print('0')
            break
        mid = (FF+EE)/2
        if 

