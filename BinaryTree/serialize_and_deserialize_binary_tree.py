# lc 297
# Definition for a binary tree node.
'''
 其实 postorder和preorder也是一样的，serialize出来的序列一模一样，只是顺序相反，所以deserialize本质也是一样的
 inorder出来的string为啥不可以deserialize，
   1） 2 as the root and 1 as the right child
   2） 1 as the root and 2 as the left child
 这两个inorder顺序一样，但是是两个不同的数
 4. 此题和lc 105类似，但是为啥lc 105需要两个顺序，因为105没有记录null，不知道叶子节点

2
  1     inorder: N 2 N 1 N   preorder: 2 N 1 N N    postorder: N N N 1 2


  1     inorder: N 2 N 1 N   preorder: 1 2 N N N    postorder: N N 2 N 1
2

两个树的inorder serialization结果是一样的, 但是preorder 和 postorder都是可以区分的
'''
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