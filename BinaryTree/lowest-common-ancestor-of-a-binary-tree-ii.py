
# lc 1644
# 和 lc 236 最大区别是p,q可能不在tree里面
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
        此题和lc 236最大不同就是不保证两个target都在树内,
        所以一定要遍历左右两个子树之后再判断当前根节点，这样才能遍历整个树的所有节点
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            nonlocal found_p, found_q
            if not root: 
                return None

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if root == p:
                found_p = True
                return root
            if root == q:
                found_q = True
                return root  

            if left and right:
                return root
            else:
                return left or right

        found_p = found_q = False
        ans = dfs(root,p,q)
        return ans if found_p and found_q else None
