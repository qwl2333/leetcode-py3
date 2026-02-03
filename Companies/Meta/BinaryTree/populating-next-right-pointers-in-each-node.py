# lc 116
from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # TC O(N)  SC O(logN) - 完美二叉树 N 个节点, 树的高度是logN
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None
        
        self.connect_helper(root.left, root.right)
        return root
    
    def connect_helper(self, node1: Optional[Node], node2: Optional[Node]):
        if not node1 or not node2:
            return

        node1.next = node2

        self.connect_helper(node1.left, node1.right)
        self.connect_helper(node1.right, node2.left)
        self.connect_helper(node2.left, node2.right)

    # TC O(N)  SC O(1)
    def connect_iterative(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root
        
        # 从根节点开始
        leftmost = root
        
        # 只要还有下一层需要连接
        while leftmost.left:
            # head 用来遍历当前这一层，连好它的孩子们
            head = leftmost
            
            while head:
                # 1. 连接同一个父节点下的两个孩子
                head.left.next = head.right
                
                # 2. 连接跨越父节点的两个孩子
                # 如果当前节点有右邻居，那么它的右儿子就要连到右邻居的左儿子
                if head.next:
                    head.right.next = head.next.left
                
                # 这一层继续向右走
                head = head.next
            
            # 这一层连完了，跳到下一层的最左边开始
            leftmost = leftmost.left
            
        return root