# lc 133
from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # BFS time O(n) - n is number of nodes in the graph, space is O(n)        
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        queue = deque([node]) # old node
        new_root = Node(node.val)
        visited = {node.val: new_root} # int - new node, if visited, means new node is created
        
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb.val not in visited:
                    queue.append(nb)
                    visited[nb.val] = Node(nb.val)

                visited[cur.val].neighbors.append(visited[nb.val])
        
        return new_root
    
    # DFS + caching   time O(n), space O(n)
    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs_clone(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            
            if node.val in old_to_new:
                return old_to_new[node.val]

            new_node = Node(node.val)
            old_to_new[node.val] = new_node
            
            for nb in node.neighbors:
                nb_copy = dfs_clone(nb)
                old_to_new[node.val].neighbors.append(nb_copy)
            
            return old_to_new[node.val]
        
        return dfs_clone(node)