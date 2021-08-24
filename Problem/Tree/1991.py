N = int(input())
TR = {}


class Node:
    def __init__(self, nd, left, right):
        self.nd = nd
        self.left = left
        self.right = right

    def lr(self):
        lf = self.left
        return lf

    def rl(self):
        rf = self.right
        return rf

    def nn(self):
        nnd = self.nd
        return nnd


def dfs(nd):
    if nd == '.':
        return
    if TR[nd].nd != '.':
        print(TR[nd].nd, end="")
        dfs(TR[nd].left)
        dfs(TR[nd].right)


def center(nd, ro):
    if nd == '.':
        return
    if TR[nd].nd != '.':
        center(TR[nd].left, nd)
        center(TR[nd].right, nd)
    print(TR[nd].nd, end="")


def last(nd):
    if nd == '.':
        return
    if TR[nd].nd != '.':
        last(TR[nd].left)
        print(TR[nd].nd, end="")
        last(TR[nd].right)


nd, ln, rn = input().split()
nnd = Node(nd, ln, rn)
TR[nd] = nnd
for _ in range(1, N):
    nd, ln, rn = input().split()
    nnd = Node(nd, ln, rn)
    TR[nd] = nnd

dfs('A')
print()
last('A')
print()
center('A', None)
