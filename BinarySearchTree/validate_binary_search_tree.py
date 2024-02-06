# lc 98
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_val = -float('inf')
        valid_bst = True
        def inorder_traverse(root: Optional[TreeNode]):
            nonlocal cur_val, valid_bst
            if valid_bst is False:
                return
            
            if not root:
                return True
            
            inorder_traverse(root.left)
            if root.val > cur_val:
                cur_val = root.val
            else:
                valid_bst = False

            inorder_traverse(root.right)
        
        inorder_traverse(root)
        return valid_bst