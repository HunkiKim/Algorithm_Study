N = int(input())
Arr = [0]
Arr1 = list(map(int, input().split()))
Arr = Arr + Arr1 + [-2] * 32
D = int(input())
Arr[D + 1] = -2
cnt = 0


def dfs(nd):
    global cnt
    if Arr[nd] == -2:
        return
    elif (Arr[nd * 2] == -2 and Arr[nd * 2 + 1] == -2 and Arr[nd] != -2):
        cnt += 1
        return
    elif Arr[nd] + 1 < Arr[nd * 2] or Arr[nd] + 1 < Arr[
            nd + 1] or Arr[nd] + 1 < Arr[nd * 2 + 1]:
        cnt += 1
        return

    dfs(nd * 2)
    dfs(nd * 2 + 1)


dfs(1)
print(cnt)