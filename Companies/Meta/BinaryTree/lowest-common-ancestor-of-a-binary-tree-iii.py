# lc 1650 和 lc160 intersection of two linkedlists类似
"""
和 lc236 lca的区别是node 定义不同, 这个有parent

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    # 最优解 space O(1) time O(h) heght of the tree logn to n
    def lowestCommonAncestor2(self, p: 'Node', q: 'Node') -> 'Node':
        i, j = p, q
        while i != j:
            i = q if not i else i.parent
            j = p if not j else j.parent
        return i
    
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

s = Solution()
n3 = Node(3)
n5 = Node(5)
n6 = Node(6)
n2 = Node(2)
n7 = Node(7)
n4 = Node(4)
n1 = Node(1)
n0 = Node(0)
n8 = Node(8)
n3.left = n5
n3.right = n1
n5.parent = n3
n1.parent = n3

res = s.lowestCommonAncestor(n3, n5)
print(res.val)
