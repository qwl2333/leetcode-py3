# lc 103
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        level = 0
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            level_order = deque()
            for _ in range(size):
                cur = queue.popleft()
                if level % 2 == 0:
                    level_order.append(cur.val)
                else:
                    level_order.appendleft(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level_order)
            level += 1
        
        return res