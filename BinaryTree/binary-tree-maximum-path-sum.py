# lc 124
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Time O(n) n - number of nodes
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -float('inf')
        def maxPathSumHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left_sum = maxPathSumHelper(root.left)
            right_sum = maxPathSumHelper(root.right)
            if left_sum < 0:
                left_sum = 0
            if right_sum < 0:
                right_sum = 0
            
            path_sum = root.val + left_sum + right_sum
            self.max_path_sum = max(self.max_path_sum, path_sum)
            return root.val + max(left_sum, right_sum)

        maxPathSumHelper(root)
        return self.max_path_sum 
