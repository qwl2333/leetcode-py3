# lc 1382
# https://www.youtube.com/watch?v=gb7WU__vyLo&ab_channel=CodeThoughts
# 看前四分钟就懂了
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # t O(n) s O(n)
    # inorder顺序得到后, 取中点为root, 左右recursively重复build bst 
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = [] # list of TreeNodes
        def inorder_traverse(root: TreeNode):
            if not root:
                return
            inorder_traverse(root.left)
            inorder.append(root)
            inorder_traverse(root.right)

        inorder_traverse(root)
        
        n = len(inorder)
        def build_balanced_bst(start: int, end: int):
            if start > end:
                return None

            mid = (start + end) // 2
            root = inorder[mid]
            root.left = build_balanced_bst(start, mid - 1)
            root.right = build_balanced_bst(mid + 1, end)

            return root
        
        return build_balanced_bst(0, n - 1)

