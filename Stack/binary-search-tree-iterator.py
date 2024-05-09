# lc 173
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    # Time O(h) h is the height of the bst, in the worst case it could be number of nodes n, when tree is skewed
    # Time O(1) avg, because there are n elements to be stored to stack, each is poped when calling next(), maybe first time a lot of nodes go into stack
    # then next time calling next(), no nodes go into stack, so avg is O(1)
    def __init__(self, root: Optional[TreeNode]):
        self.head = root
        self.stack = list()

    def next(self) -> int:
        while self.head: # looks like O(n), but all nodes only go into stack 1 time, so in total n nodes in stack, avg time is O(1)
            self.stack.append(self.head)
            self.head = self.head.left
        cur = self.stack.pop()
        self.head = cur.right
        return cur.val

    def hasNext(self) -> bool:
        if not self.stack and not self.head:
            return False

        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()