A = int(input())
L = [] # list
for i in range(A):
    L.append(int(input()))
C = [0 for _ in range(A)] #count 
B = [0 for _ in range(A)] #답 memozation
C[0] = 1
B[0] = L[0]
for i in range(1,A):
    if C[i-1] < 2:
        B[i] = B[i-1] + L[i]
        C[i] = C[i-1] + 1
        #print('1')
    else:
        if B[i-1] >= L[i] + L[i-1] + B[i-3] and B[i-1]>L[i] + B[i-2]:
            B[i] = B[i-1]
            C[i] = 0
            #print('2')
        elif L[i] + B[i-2] >= L[i] + L[i-1] + B[i-3]:
            B[i] = L[i] + B[i-2]
            C[i] = 1
            #print('3')
        else :
            C[i] = C[i-1] + 1
            B[i] = L[i] + L[i-1] + B[i-3]
            
print(B[A-1])