# lc 543  post order traversal, time O(n), space O(n)- worst case like a skewed tree 
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_height(root)
        return self.max_diameter
        
    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height, right_height = self.get_height(root.left), self.get_height(root.right) 

        self.max_diameter = max(self.max_diameter, left_height + right_height)

        return max(left_height, right_height) + 1