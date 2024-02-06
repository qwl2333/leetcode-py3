# lc 235
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Recursive Time O(logn)每次都是左右选一个， space if not couting stack frames O(1), o/w O(logn) worst case O(n) when tree is skewed
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        
        if root == p or root == q:
            return root
        
        if root.val > p.val and root.val < q.val:
            return root
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, q, p)
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, q, p)
        
    # Iterative time O(logn), space O(1)
    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        
        cur = root
        while cur:
            if cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val:
                cur = cur.right
            else: # (cur.val > p.val and cur.val < q.val) or cur.val == p.val or cur.val == q.val
                return cur
        
        return cur