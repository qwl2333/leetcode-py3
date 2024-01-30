# lc 226
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Since each node in the tree is visited only once, 
    # the time complexity is O(n), where n is the number of nodes in the tree. 
    # We cannot do better than that, since at the very least we have to visit each node to invert it.
    # Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. 
    # Because h ∈ O(n), the space complexity is O(n). 
    # In the worst scenario, each level only have one node, h = n
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root

s = Solution()
node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
print(s.invertTree(node1).left.val)