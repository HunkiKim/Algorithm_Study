A = int(input())
C = ''
count = 10
count2 = 1
ans = 0
while True:
    if count-1<A: # 1~9숫자 길이 1 -> 10~99숫자 길이2 -> 100~999숫자 길이3
        ans += (count-1)*count2 - (count/10 -1)*(count2) 
        count *=10 #숫자 
        count2 += 1 #길이
    else: # 120 -> 1~9 10~99 100~999 120
        #A=120 100-1 = 99 100~120
        ans += (A - (count/10-1))*count2
        break
        
print(int(ans))