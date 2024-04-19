# lc 314
from collections import defaultdict, deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root: # root is None
            return []
        col_to_nodes = defaultdict(list) # key: col number, value: list[int]
        min_col = float('inf')
        max_col = -float('inf')
        queue = deque([(root, 0)])

        while queue:
            node, col_number = queue.popleft()
            min_col, max_col = min(min_col, col_number), max(max_col, col_number)
            col_to_nodes[col_number].append(node.val)
            if node.left:
                queue.append((node.left, col_number - 1))
            if node.right:
                queue.append((node.right, col_number + 1))

        res = []
        for i in range(min_col, max_col + 1):
            res.append(col_to_nodes[i])
        return res
