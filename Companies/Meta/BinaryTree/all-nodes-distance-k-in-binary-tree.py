# lc 863
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解题思路：把树变成图 (Graph BFS)
# 最直观的解法分为两步：

# 1 建立父节点映射 (Build Parent Map)：

# 因为 TreeNode 没有 parent 指针，我们需要遍历一次树（DFS），用一个哈希表（字典）记录每个节点的父节点：parent_map[node] = node.parent。

# 这样，二叉树就变成了一个无向图：每个节点可以通向 left, right, 和 parent。

# 2 层序遍历 (BFS) 找第 K 层：

# 从 target 节点开始进行 BFS。

# 这就变成了标准的“图的最短路径”问题。我们向三个方向（左子、右子、父节点）扩散。

# 当扩散了 k 步时，队列里剩下的所有节点就是答案。

# 注意：需要一个 visited 集合，避免走回头路（比如从父节点下来，又跑回父节点）。
from collections import deque

class Solution:
    # Time Space both O(n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        # 1. 构建父节点映射 (DFS)
        parents = {}

        def add_parents(node: TreeNode, parent: TreeNode):
            if not node:
                return
            
            parents[node] = parent
            add_parents(node.left, node)
            add_parents(node.right, node)
        
        add_parents(root, None)

        # 2. 从 target 开始 BFS
        queue = deque([target])
        visited = set([target])
        current_distance = 0

        while queue:
            # 如果当前扩散距离已经是 k，队列里剩下的就是答案
            if current_distance == k:
                return [node.val for node in queue]

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for nb in (node.left, node.right, parents[node]):
                    if nb and nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            
            current_distance += 1
        
        return []