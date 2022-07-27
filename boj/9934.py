# pypy3 114328kb / 120ms

import sys
input = sys.stdin.readline

# inorder
# 노드 갯수는 2^k - 1

'''
                1(n)
        2(2n)            3(2n + 1)
4(2n * 2)   5(2n * 2 + 1)
'''

k = int(input())
nodes = list(map(int, input().split()))
n = 2 ** k
tree = [0] * n # 0번인덱스는 안씀
idx = 0

def inorder(node):
    global idx
    
    if node < n:
        inorder(node * 2) # left
        tree[node] = nodes[idx] # root
        idx += 1
        inorder(node * 2 + 1) # right


inorder(1)
idx = 1
while idx < n:
    for i in range(idx, idx * 2):
        print(tree[i], end = ' ')
    print()
    idx *= 2