# lc 987
# https://www.youtube.com/watch?v=_8yW-dQVJHM&ab_channel=CrackingFAANG
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
# time O(nlogn/k) 虽然实际是sort重合的点， sort 肯定是close to nlogn的。所以说nlogn也没问题
# space O(n)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((0, 0, root))
        col_to_nodes: dict[int, dict[int, list]] = {} # 也可以直接加 dict[col, tuple[r, val]] 最后的for loop再sort tuple也行
        min_col, max_col = float('inf'), -float('inf')
        while queue:
            r, c, root = queue.popleft()
            min_col, max_col = min(min_col, c), max(max_col, c)
            if c not in col_to_nodes:
                col_to_nodes[c] = {}
            if r not in col_to_nodes[c]:
                col_to_nodes[c][r] = []
            col_to_nodes[c][r].append(root.val)

            if root.left:
                queue.append((r + 1, c - 1, root.left))
            if root.right:
                queue.append((r + 1, c + 1, root.right))
        
        res = []
        for col in range(min_col, max_col + 1):
            res.append([])
            row_to_nodes = col_to_nodes[col]
            for _row, val_list in row_to_nodes.items():
                if len(val_list) > 0:
                    val_list.sort()
                res[col - min_col].extend(val_list)
        
        return res