A,B = map(int, input().split())
ANS = [2,3]
flag = True
if B<=3:
    for i in range(A,B+1):
        if i!=1:
            print(i)
    exit()
if A==3:
    print('3')
elif A<3:
    print('2')
    print('3')


for i in range(4,B+1):
    for j in ANS:
        if i%j == 0:
            flag = False
    if flag == True:
        ANS.append(i)
    else:
        flag= True

for i in ANS:
    if i>=A:
        print(i)

