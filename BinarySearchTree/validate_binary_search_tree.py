# lc 98
from typing import Optional, Tuple
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
                return
            
            inorder_traverse(root.left)
            if root.val > cur_val:
                cur_val = root.val
            else:
                valid_bst = False

            inorder_traverse(root.right)
        
        inorder_traverse(root)
        return valid_bst

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        MIN_VAL = -float('inf')
        MAX_VAL = float('inf')
        def is_valid_bst_helper(root: Optional[TreeNode]) -> Tuple[float, float, bool]:
            if not root:
                return (MAX_VAL, MIN_VAL, True)
            
            min_l, max_l, is_l_bst = is_valid_bst_helper(root.left)
            min_r, max_r, is_r_bst = is_valid_bst_helper(root.right)
            if is_l_bst and is_r_bst and max_l < root.val < min_r:
                min_of_cur = min_l if min_l != MAX_VAL else root.val
                max_of_cur = max_r if max_r != MIN_VAL else root.val
                return (min_of_cur, max_of_cur, True)
            else:
                return (MAX_VAL, MIN_VAL, False)
        
        _min, _max, is_bst = is_valid_bst_helper(root)
        return is_bst