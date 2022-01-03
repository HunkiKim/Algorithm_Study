from collections import deque

H1 = deque()
H2 = deque()
H3 = deque()
N = int(input())
for i in range(1, N + 1):
    H1.appendleft(i)
cnt = 0


def dfs(num, h):
    global N
    global cnt
    cnt += 1

    print(h, num)
    if N == len(H3) or cnt == 7:
        print(H3, H2, H1)
        exit(0)
    if h == 1:
        flag2 = False
        if len(H3) != 0:
            if H3[-1] > num:
                H3.append(num)
                flag2 = True
        elif len(H3) == 0:
            H3.append(num)
            flag2 = True
        if flag2 == False:
            H2.append(num)
    elif h == 2:
        flag2 = False
        if len(H1) != 0:
            if H1[-1] > num:
                H1.append(num)
                flag2 = True
        elif len(H1) == 0:
            H1.append(num)
            flag2 = True
        if flag2 == False:
            H3.append(num)
    elif h == 3:
        flag2 = False
        if len(H2) != 0:
            if H2[-1] > num:
                H2.append(num)
                flag2 = True
        elif len(H2) == 0:
            H2.append(num)
            flag2 = True
        if flag2 == False:
            H1.append(num)
    print(H1, H2, H3)
    flag = False
    if len(H1) != 0:
        if len(H3) == 0:
            dfs(H1.pop(), 1)
            flag = True
        elif len(H3) != 0:
            if H1[-1] < H3[-1]:
                dfs(H1.pop(), 1)
                flag = True
        if flag == False:
            if len(H2) == 0:
                dfs(H1.pop(), 1)
                flag = True
            elif len(H2) != 0:
                if H1[-1] < H2[-1]:
                    dfs(H1.pop(), 1)
                    flag = True
    if len(H3) != 0 and flag == False:
        if len(H2) == 0:
            dfs(H3.pop(), 3)
            flag = True
        elif len(H2) != 0:
            if H3[-1] < H2[-1]:
                dfs(H3.pop(), 3)
                flag = True
        # if flag == False:
        #     if len(H1) == 0:
        #         dfs(H3.pop(), 3)
        #         flag = True
        #     elif len(H1) != 0:
        #         if H3[-1] < H1[-1]:
        #             dfs(H3.pop(), 3)
        #             flag = True
    if len(H2) != 0 and flag == False:
        if len(H3) == 0:
            dfs(H2.pop(), 2)
            flag = True
        elif len(H3) != 0:
            if H2[-1] < H3[-1]:
                dfs(H2.pop(), 2)
                flag = True
        if flag == False:
            if len(H1) == 0:
                dfs(H2.pop(), 2)
                flag = True
            elif len(H1) != 0:
                if H2[-1] < H1[-1]:
                    dfs(H2.pop(), 2)
                    flag = True
    


dfs(H1.pop(), 1)
print(H3)