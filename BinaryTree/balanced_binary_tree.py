# lc 110
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time complexity: O(n) The algorithm performs a depth-first traversal of the binary tree, visiting each node once.
    # Space complexity: O(h), where h is the height of the binary tree
    # The space complexity is determined by the maximum height of the call stack during the recursive DFS traversal.
    # In the worst case, when the tree is skewed (completely unbalanced), the space complexity is O(n).
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.is_balanced_helper(root)
        return balanced

    def is_balanced_helper(self, root: Optional[TreeNode]) -> (bool, int): # Tuple[bool, int]
        if root is None:
            return (True, 0)
    
        right_balanced, right_height = self.is_balanced_helper(root.right)
        if right_balanced is False:
            return (False, 0)
          
        left_balanced, left_height = self.is_balanced_helper(root.left)

        if right_balanced and left_balanced:
            if abs(right_height - left_height) <= 1:
                return (True, max(right_height, left_height) + 1)
            else:
                return (False, 0)
        else:
            return (False, 0)
