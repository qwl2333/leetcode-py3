# lc 103
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/750132/four-python-solutions/
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

    # 真正的zigzag traversal就是pop出来的顺序就是zigzag的
    def zigzagLevelOrder2(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        queue = deque([root]) # 秘诀就是用deque
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                if even_level:
                    # pop from right and append from left.
                    node = queue.pop()
                    # to maintain the order of nodes in the format of [left, right, left, right] 
                    # we push right first since we are appending from left
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                else:
                    # pop from left and append from right
                    node = queue.popleft()
                    # here the order is maintained in the format [left, right, left, right] 
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                level.append(node.val)
            res.append(level)
            even_level = not even_level
        return res