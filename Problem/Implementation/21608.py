import sys
# 1. 좋아하는애 많은곳 ( 우선도 젤높)
# 2. 똑같으면 빈칸 더 많은곳 (+ 해주기)
# 3. 행, 열 순서대로 (3순위)
# tuple로 좋,똑,행,열 넣기
input = sys.stdin.readline
N = int(input())
L = [[0] * N for _ in range(N)]
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
D = {}
for k in range(N * N):  # 입력
    l = list(map(int, input().split()))
    ll = l[1:]  # 인풋받은거 맨앞 빼고
    f = l[0]  # 맨앞
    D[f] = ll
    l2 = list()  # 주변 다 확인 한애들 넣어좋고 솔트용
    for i in range(N):  # y
        for j in range(N):  # x
            a1 = 0  # 1번
            a2 = 0  # 2번
            y1 = i  # 3-1 행
            x1 = j  # 3-2 열
            if L[i][j] != 0:
                continue
            for t in range(4):  # 주변확인
                nx = x[t] + j
                ny = y[t] + i
                if 0 <= nx < N and 0 <= ny < N:
                    flag = False
                    if ll.count(L[ny][nx]) > 0:
                        a1 += 1

                    elif L[ny][nx] == 0:
                        a2 += 1
            l2.append((a1, a2, y1, x1))  # 해당 결과를 저장
    l2.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))  # 조건 순서대로 정렬
    L[l2[0][2]][l2[0][3]] = f  # 제일 조건 조흥ㄴ곳에 저장
ans = 0
for i in range(N):
    for j in range(N):
        p = 0
        l3 = D[L[i][j]]
        for k in range(4):
            nx = j + x[k]
            ny = i + y[k]
            if 0 <= nx < N and 0 <= ny < N:
                if l3.count(L[ny][nx]) > 0:
                    p += 1
        if p == 1:
            ans += 1
        elif p == 2:
            ans += 10
        elif p == 3:
            ans += 100
        elif p == 4:
            ans += 1000
print(ans)
