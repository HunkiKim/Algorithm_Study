import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None


def dfs(num, tree):
    if num < tree.data:
        if tree.left == None:
            tree.left = Node(num, tree.data)
            return
        else:
            dfs(num, tree.left)
    else:
        if tree.right == None:
            tree.right = Node(num, tree.data)
            return
        else:
            dfs(num, tree.right)


def postorder(tree):
    if tree.left != None:
        postorder(tree.left)
    if tree.right != None:
        postorder(tree.right)
    print(tree.data)


dq = deque()
num = int(input())
root = Node(num, 0)
while True:
    try:
        num = int(input())
        dfs(num, root)
    except:
        break
postorder(root)
