# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    length: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return -1 

            left = dfs(root.left)
            right = dfs(root.right)

            self.length = max(self.length, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.length
