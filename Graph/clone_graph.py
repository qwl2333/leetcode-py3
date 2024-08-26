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
                if nb.val not in visited: # visited 针对的是未访问过的node，但是依然需要把所有的边关系都添加到新的node，所以才有28行，不管这个nb有没有被visited过，边信息都是要添加的，因为是无向图，边信息肯定要两个node都加一下
                    queue.append(nb)
                    visited[nb.val] = Node(nb.val)

                visited[cur.val].neighbors.append(visited[nb.val])
        
        return new_root
    
    # DFS + caching   time O(n), space O(n)
    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        def clone_helper(node: Optional['Node'], visited: dict) -> Optional['Node']:
            if not node:
                return None
            if node.val in visited:
                return visited[node.val]

            new_node = Node(node.val)
            visited[node.val] = new_node

            for nb in node.neighbors:
                nb_new = clone_helper(nb, visited)
                new_node.neighbors.append(nb_new)
            
            return new_node

        return clone_helper(node, {})

s = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
new_node1 = s.cloneGraph(node1)
print(new_node1.val)
print(new_node1.neighbors[1].val)