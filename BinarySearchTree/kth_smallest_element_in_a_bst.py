# lc 230
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.i = 0
        self.res = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traverse(root: Optional[TreeNode]):
            if not root:
                return
            if self.i > k:
                return
            inorder_traverse(root.left)

            self.i += 1
            if self.i == k:
                self.res = root.val

            inorder_traverse(root.right)
        
        inorder_traverse(root)
        return self.res
        