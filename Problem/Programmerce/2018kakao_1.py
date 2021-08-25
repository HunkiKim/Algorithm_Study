def solution(dartResult):
    answer = 0
    L = list()
    T = list()
    flag = False
    for i in range(len(dartResult)):
        if flag == True:
            flag = False
            L.append(T)
            T = list()
            T.append("10")
            continue
        if dartResult[i].isdigit():
            if dartResult[i + 1] == '0':
                flag = True
                continue
            L.append(T)
            T = list()
            T.append(dartResult[i])
        else:
            T.append(dartResult[i])
    print(L)
    if len(T) != 0:
        L.append(T)
    for i in range(1, len(L)):
        num = 1

        for j in L[i]:
            if j.isdigit():
                num = num * int(j)
            elif j == "#":
                num = num * -1
            elif j == '*':
                num *= 2
            elif j == "D":
                num = num**2
            elif j == "T":
                num = num**3
            elif j == "S":
                num = num**1
        if i != len(L) - 1:
            if L[i + 1].count('*'):
                num *= 2
        print(num)
        answer += num
    return answer
    #20