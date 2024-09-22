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
        self.sum_bst = 0
        def rangeSumBSTHelper(root: Optional[TreeNode]):
            if not root:
                return
            if root.val < low:
                rangeSumBSTHelper(root.right)
            elif root.val > high:
                rangeSumBSTHelper(root.left)
            else: # low <= root.val <= high
                self.sum_bst += root.val
                rangeSumBSTHelper(root.left)
                rangeSumBSTHelper(root.right)
        rangeSumBSTHelper(root)
        return self.sum_bst