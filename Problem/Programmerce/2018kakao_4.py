def solution(m, n, board):
    board1 = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            board1[j].append(board[i][j])
    for i in range(m):
        board1[i].reverse()
    if m == 1 or m == 0:
        return 0
    cnt=0
    while True:
        L = list()
        for i in range(n - 1):
            for j in range(m - 1):
                if board1[i][j] == board1[i][j + 1] == board1[
                        i + 1][j] == board1[i + 1][j +
                                                   1] and board1[i][j] != "":
                    L.append((i, j))
        if len(L) == 0:
            break
        L.sort(key=lambda x: (-x[1], x[0]))

        for i in L:
            x = i[0]
            y = i[1]
            
            board1[x][y] = ""
            board1[x + 1][y] = ""
            board1[x][y + 1] = ""
            board1[x + 1][y + 1] = ""

        for i in range(n):
            c = 0
            for j in range(m):
                if board1[i][j - c] == "":
                    
                    del board1[i][j - c]
                    board1[i].append("")
                    c += 1
    for i in board1:
        for j in i:
            if j=="":
                cnt+=1
    return cnt


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
