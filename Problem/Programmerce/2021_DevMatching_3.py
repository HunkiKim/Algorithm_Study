def solution(enroll, referral, seller, amount):
    answer = []
    D = {}
    D["center"] = []
    M = {}
    M["center"] = 0
    for i in enroll:
        M[i] = 0
    for i,j in zip(enroll, referral):
        if j == "-":
            D[i] = "center"
        else:
            D[i] = j
    for i,j in zip(seller, amount):
        sell = D[i]
        money = j*100
        ten_money = money // 10
        M[i] += (money-ten_money)
        money = ten_money
        while True:
            if money == 0:
                break
            if sell == "center":
                M["center"] += money
                break
            ten_money = money // 10
            M[sell] += (money-ten_money)
            money = ten_money
            sell = D[sell]
    for i in M:
        if i=='center':
            continue
        answer.append(M[i])
    return answer
