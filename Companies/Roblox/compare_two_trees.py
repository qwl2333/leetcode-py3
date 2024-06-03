# similar to 872 leaf-similar trees
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val='', children=[]):
        self.val = val
        self.children = children

# default val is '', only leaf node has a text inside val
# compare two trees to see if they are similar
# similar means leaf nodes of two trees have same values

class Traversor:
    def are_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse_helper(root: Optional[TreeNode], leaves: list[str]):
            if not root:
                return

            if root.val != '':
                leaves.append(root.val)

            for child in root.children:
                traverse_helper(child, leaves)
        
        leaves1 = []
        leaves2 = []
        traverse_helper(root1, leaves1)
        traverse_helper(root2, leaves2)
        return sorted(leaves1) == sorted(leaves2)