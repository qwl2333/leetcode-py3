# lc 1650
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    # Time O(l) l - depth of tree, Space O(l), in the wase case, if tree is skewed, l = n, n is number of nodes in the tree
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cur = p
        p_path = set()
        while cur:
            p_path.add(cur)
            cur = cur.parent

        cur = q
        while cur:
            if cur in p_path:
                return cur
            cur = cur.parent
        return None
