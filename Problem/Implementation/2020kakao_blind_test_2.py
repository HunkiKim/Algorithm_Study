def u__split(u):
    if u=="":
        return ""
    u_split = [u[0]]
    cnt = 0
    for i in range(1,len(u)):
        if not u_split:
            cnt = i
            break
        elif u_split[-1] == "(" and u[i] == ")":
            u_split.pop()
        elif u_split[-1] == ")" and u[i] == "(":
            u_split.pop()
        else:
            u_split.append(u[i])
    if cnt==0:
        cnt = len(u)
    us = u[:cnt]
    vs = u[cnt:]
    u_tmp = [us[0]]
    cnt = 0
    for i in range(1,len(us)):
        if not u_tmp:
            u_tmp.append(us[i])
        elif u_tmp[-1] == "(" and us[i] == ")":
            u_tmp.pop()
        else:
            u_tmp.append(us[i])
    if not u_tmp:
        st = ''.join(us) + u__split(''.join(vs))
        return st
    else:
        st = "(" + u__split(''.join(vs)) + ")"
        u_reverse = ""
        for i in range(1,len(us)-1):
            if us[i] == "(":
                u_reverse += ")"
            else:
                u_reverse += "("
        st += u_reverse
        return st
def solution(p):
    answer = ""
    answer = u__split(p)
    return answer
