# lc 199
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            num_nodes_level = len(queue)
            for i in range(num_nodes_level):
                cur = queue.popleft()
                if i == num_nodes_level - 1:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return res  
    
    # preorder, but it is root, right, left
    # Time O(n), space O(n) - whether stack frames considered
    def rightSideViewRecursion(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        def traverse(root: Optional[TreeNode], depth: int) -> None:
            if not root:
                return
            
            if depth == len(res):
                res.append(root.val)
            
            traverse(root.right, depth + 1)
            traverse(root.left, depth + 1)
            return

        traverse(root, 0)
        return res