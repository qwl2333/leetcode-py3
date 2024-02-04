# lc 105
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time O(n), Space n for map, logn ~ n is the height of tree, also stack frames, which combines to O(n) 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_to_index = {}
        for i, num in enumerate(inorder):
            value_to_index[num] = i

        def build_tree_helper(preorder: List[int], inorder: List[int], pre_start: int, in_start, in_end: int) -> Optional[TreeNode]:
            if in_start > in_end:
                return None

            # find root index of preorder[start] in inorder
            root_index_in = value_to_index[preorder[pre_start]]
            left_num_nodes = root_index_in - in_start

            left_subtree = build_tree_helper(preorder, inorder, pre_start + 1, in_start, root_index_in - 1)
            right_subtree = build_tree_helper(preorder, inorder, pre_start + left_num_nodes + 1, root_index_in + 1, in_end)
            
            root = TreeNode(preorder[pre_start])
            root.left = left_subtree
            root.right = right_subtree
            return root
        
        return build_tree_helper(preorder, inorder, 0, 0, len(inorder) - 1)