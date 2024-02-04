# lc 104
from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
    
    # iterative做法，是利用level order traverse
    def max_depth_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        num_nodes_level = 1 # counter to counter how many nodes each level
        levels = 0
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            num_nodes_level -= 1
            if num_nodes_level == 0:
                num_nodes_level = len(queue)
                levels += 1
        return levels



s = Solution()
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
print(s.max_depth_iterative(node1))