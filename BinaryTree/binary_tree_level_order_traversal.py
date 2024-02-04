# lc 102
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # time O(n), space O(n/2) 假如是1，2，4，2^h - 总和为2^(h+1)，一共这么多节点，最多一层可以有2^h
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            num_nodes_level = len(queue)
            level_list = []
            for i in range(num_nodes_level):
                cur = queue.popleft()
                level_list.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level_list)                      
            
        return res  

s = Solution()
node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
print(s.levelOrder(node1)) 