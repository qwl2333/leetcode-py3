# lc 173
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    # Time O(h) h is the height of the bst, in the worst case it could be number of nodes n, when tree is skewed
    # Time O(1) avg, because there are n elements to be stored to stack, each is poped when calling next(), maybe first time a lot of nodes go into stack
    # then next time calling next(), no nodes go into stack, so avg is O(1)
    def next(self) -> int:
        cur = self.stack.pop()
        right = cur.right
        while right:
            self.stack.append(right)
            right = right.left
        return cur.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()