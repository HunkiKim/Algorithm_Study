def binary(num, n):
    ans = ""

    while True:
        if num % 2 == 0:
            num = num // 2
            ans = "0" + ans
        elif num % 2 == 1:
            num = num // 2
            ans = "1" + ans
        if num == 1 or num == 0:
            break
    if num == 1:
        ans = "1" + ans
    else:
        ans = "0" + ans
    if len(ans) != n:
        ans = "0" * (n - len(ans)) + ans
    return ans


def solution(n, arr1, arr2):
    answer = []
    L1 = list()
    L2 = list()
    L3 = [[0] * n for _ in range(n)]
    print(arr1, arr2)
    for i in arr1:
        L1.append(binary(i, n))
    for i in arr2:
        L2.append(binary(i, n))
    for i in range(n):
        for j in range(n):
            if L1[i][j] == "1" or L2[i][j] == "1":
                L3[i][j] = 1
    answer = list()
    for i in L3:
        T = ""
        for j in i:
            if j == 1:
                T = T + "#"
            else:
                T = T + " "
        answer.append(T)
    return answer


#40시작
# 20분