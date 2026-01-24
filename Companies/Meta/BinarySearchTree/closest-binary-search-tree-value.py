# lc 270
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.dist = float('inf')
        self.res = 0
        def search_target(root: Optional[TreeNode]):
            if not root:
                return
            
            if target == root.val:
                self.res = root.val
                self.dist = 0
                return

            if self.dist > abs(root.val - target):
                self.dist = abs(root.val - target)
                self.res = root.val

            if self.dist == abs(root.val - target):
                self.res = min(self.res, root.val)

            if target > root.val:
                search_target(root.right)
            
            if target < root.val:
                search_target(root.left)
            
        search_target(root)
        return self.res
    
    # 我更喜欢这个解法
    def closestValueIterative(self, root: Optional[TreeNode], target: float) -> int:
        dist = float('inf')
        nearest_node = 0

        while root:
            if root.val == target:
                return root.val
            
            if abs(root.val - target) < dist:
                dist = abs(root.val - target)
                nearest_node = root.val
            
            if abs(root.val - target) == dist:
                nearest_node = min(nearest_node, root.val)
            
            if root.val > target:
                root = root.left
            else: # root.val < target
                root = root.right
        
        return nearest_node