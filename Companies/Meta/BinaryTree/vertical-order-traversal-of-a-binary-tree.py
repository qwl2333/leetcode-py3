# lc 987
# https://www.youtube.com/watch?v=_8yW-dQVJHM&ab_channel=CrackingFAANG
# Definition for a binary tree node.
'''
和314的区别
314的vertical order是固定的top to bottom, left to right if row,col are the same
987的vertical order是top to bottom, if row, col are the same, sort by value
所以在添加一个col比如0的vertical order时, 必须按照row从低到高添加, 而且同col同row必须sort by value
所以需要记录row的信息, 虽然在添加时用不到row只需要知道此row对应的list of values
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
# time O(n + nlog(n/k)) n is the number of nodes in the tree, k is the width of the tree, or number of columns in the result, if the tree is skewed, k equals n in this case, time is O(n)
# 虽然实际是sort重合的点， sort 肯定是close to nlogn的。所以说nlogn也没问题
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
            for _row, val_list in row_to_nodes.items(): # dict key的顺序是添加的顺序, 所以row_to_nodes的row一定是从小到大,因为添加的顺序是从0开始一层层变大的
                if len(val_list) > 0:
                    val_list.sort()
                res[col - min_col].extend(val_list)
        
        return res