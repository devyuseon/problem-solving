# pypy3 113112kb / 112ms

import sys
input = sys.stdin.readline

def preorder(root):
    if root != '.':
        print(root, end = '')
        left, right = tree[root]
        preorder(left)
        preorder(right)
        
def inorder(root):
    if root != '.':
        left, right = tree[root]
        inorder(left)
        print(root, end = '')
        inorder(right)
    
def postorder(root):
    if root != '.':
        left, right = tree[root]
        postorder(left)
        postorder(right)
        print(root, end = '')
    
n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
    
preorder('A')
print()
inorder('A')
print()
postorder('A')