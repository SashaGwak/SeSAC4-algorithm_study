# 1991 트리 순회

import sys

N = int(sys.stdin.readline().strip())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

# root -> left -> right
def preorder(root):
    if root != ".":
        print(root, end="") # root
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

# left -> root -> right
def inorder(root):
    if root != ".":
        inorder(tree[root][0]) #left
        print(root, end="") # root
        inorder(tree[root][1]) # right

# left -> right -> root
def postorder(root):
    if root != ".":
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root, end="") #root

preorder("A")
print()
inorder("A")
print()
postorder("A")