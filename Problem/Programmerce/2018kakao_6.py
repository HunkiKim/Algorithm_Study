def solution(str1, str2):
    R = 65536
    answer = 0
    L1 = {}
    L2 = {}
    s1 = str1.lower()
    s2 = str2.lower()
    for i in range(len(s1) - 1):
        if s1[i].isalpha() and s1[i + 1].isalpha():
            s = s1[i] + s1[i + 1]
            if s not in L1:
                L1[s] = 1
            else:
                L1[s] += 1
    for i in range(len(s2) - 1):
        if s2[i].isalpha() and s2[i + 1].isalpha():
            s = s2[i] + s2[i + 1]
            if s not in L2:
                L2[s] = 1
            else:
                L2[s] += 1
    gyo = 0
    hap = 0
    for i in L1:
        if i in L2:
            gyo += min(L1[i], L2[i])
            hap += max(L1[i], L2[i])
        else:
            hap += L1[i]
    for i in L2:
        if i not in L1:
            hap += L2[i]
    print(hap)
    print(gyo)
    if hap != 0:
        answer = int((gyo / hap) * R)
    else:
        answer = R
    return answer


# 10분컷