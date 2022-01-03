N = int(input())
L = 0b00000000000000000000
for i in range(21):
    L.append(0)
for i in range(N):
    inp = input()
    if inp == 'all':
        L = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        continue
    elif inp == 'empty':
        L = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        continue
    o,x = inp.split()
    if o == 'add':
        L[int(x)] = 1
    elif o == 'remove':
        L[int(x)] = 0
    elif o == 'check':
        print(L[int(x)])
    elif o == 'toggle':
        if L[int(x)]==0:
            L[int(x)] = 1
        else:
            L[int(x)] = 0
    