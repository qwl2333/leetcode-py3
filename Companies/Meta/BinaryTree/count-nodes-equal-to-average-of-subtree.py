# lc 2265
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # T o(n) space O(h) height of tree h = logn - n so space is O(logn) -> O(n)
        def averageOfSubtreeHelper(root: TreeNode) -> tuple: # (eligible nodes, sum, num of nodes)
            """
            递归计算子树的统计信息。
            返回一个包含 (满足条件的节点数, 总和, 节点总个数) 的命名元组。
            """
            if not root:
                return (0, 0, 0)
            
            l_valid_nodes, l_sum, l_nodes = averageOfSubtreeHelper(root.left)
            r_valid_nodes, r_sum, r_nodes = averageOfSubtreeHelper(root.right)

            if root.val == (l_sum + r_sum + root.val) // (l_nodes + r_nodes + 1):
                return (l_valid_nodes + r_valid_nodes + 1, l_sum + r_sum + root.val, l_nodes + r_nodes + 1)
            else:
                return (l_valid_nodes + r_valid_nodes, l_sum + r_sum + root.val, l_nodes + r_nodes + 1)
        
        return averageOfSubtreeHelper(root)[0]

            