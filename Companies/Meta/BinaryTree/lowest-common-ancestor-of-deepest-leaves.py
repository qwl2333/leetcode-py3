# lc 1123
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lcaDeepestLeavesHelper(root: Optional[TreeNode]) -> tuple[int, TreeNode]:
            if not root:
                return (-1, None)

            l_h, l_lca = lcaDeepestLeavesHelper(root.left)
            r_h, r_lca = lcaDeepestLeavesHelper(root.right)
            if l_h > r_h:
                return (l_h + 1, l_lca)
            elif l_h < r_h:
                return (r_h + 1, r_lca)
            else: # l_h == r_h
                return (r_h + 1, root)

        
        _h, lca = lcaDeepestLeavesHelper(root)
        return lca

