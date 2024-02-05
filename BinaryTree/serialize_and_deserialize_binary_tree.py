# lc 297
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.i = 0

    # Time O(n) n - how many roots do we have, space O(n) stack frames
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder_traverse(root: TreeNode):
            if not root:
                res.append('N')
                return None
            res.append(str(root.val))
            preorder_traverse(root.left)
            preorder_traverse(root.right)
            
        preorder_traverse(root)
        return ','.join(res)
        

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0
        def build_binary_tree(vals: list) -> TreeNode:
            if vals[self.i] == 'N':
                self.i += 1
                return None

            root = TreeNode(int(vals[self.i]))
            self.i += 1
            root.left = build_binary_tree(vals)
            root.right = build_binary_tree(vals)
            return root
        
        return build_binary_tree(vals)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))