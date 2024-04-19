# lc 426
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time O(n), worst case space O(n), tree is skewed
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        head = Node(0) # dummy node as head
        self.cur = head # use this self.cur to traverse all nodes in BST

        def inorder_traverse(root: 'Optional[Node]'):
            if not root:
                return
            
            inorder_traverse(root.left)

            print(root.val)
            self.cur.right = root
            root.left = self.cur
            self.cur = root
            

            inorder_traverse(root.right)
        
        inorder_traverse(root)
        first_node = head.right
        self.cur.right = first_node
        first_node.left = self.cur
        return first_node
