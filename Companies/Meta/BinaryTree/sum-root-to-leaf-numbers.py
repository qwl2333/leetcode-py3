# lc 129
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def preorder(root: Optional[TreeNode], val: int):
            if not root:
                return
            
            val = val * 10 + root.val
            if not root.left and not root.right:
                self.sum += val

            preorder(root.left, val)
            preorder(root.right, val)
        preorder(root, 0)
        return self.sum