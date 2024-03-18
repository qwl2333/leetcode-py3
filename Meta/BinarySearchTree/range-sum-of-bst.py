# lc 938
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time O(n) n - number of nodes, worst case all nodes will be traversed, space O(h) h - height of the tree
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0

        def traverse(root: Optional[TreeNode]):
            if not root:
                return
            
            if low <= root.val <= high:
                self.res += root.val
            
            if low < root.val < high:
                traverse(root.left)
                traverse(root.right)
            elif root.val <= low:
                traverse(root.right)
            else: # root.val >= high
                traverse(root.left)

        traverse(root)   
        return self.res