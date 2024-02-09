# lc 323
from collections import deque
class Solution:
    # Union find time O(n * m) n - number of nodes, m - number of edges, space O(n)
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents = [i for i in range(n)]
        num_of_components = n

        def find_parent(parents: list[int], i): # time O(n) n - number of nodes
            if parents[i] == i:
                return i
            else:
                return find_parent(parents, parents[i])
        
        for e in edges:
            p1 = find_parent(parents, e[0])
            p2 = find_parent(parents, e[1])
            if p1 != p2: # 可以用来找环，p1 == p2 证明有环
                parents[p1] = p2
                num_of_components -= 1

        return num_of_components
    
    # dfs time O(n + m) 所有边和节点刚好遍历一次, space O(n + m) adjacent list
    def countComponentsDFS(self, n: int, edges: list[list[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for s, e in edges: 
            graph[s].append(e)
            graph[e].append(s)
        
        components = 0
        visited = set()
        def dfs(node: int):
            if node in visited:
                return

            visited.add(node)
            for nb in graph[node]:
                dfs(nb)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components
    
    # bfs time O(n + m), space O(n + m) adjacent list
    def countComponentsBFS(self, n: int, edges: list[list[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for s, e in edges: 
            graph[s].append(e)
            graph[e].append(s)
        
        components = 0
        visited = set()
        def bfs(node: int):
            if node in visited:
                return
            queue = deque([node])
            visited.add(node)
            while queue:
                cur = queue.popleft()
                for nb in graph[cur]:
                    if nb not in visited:
                        queue.append(nb)
                        visited.add(nb)
                
        
        for i in range(n):
            if i not in visited:
                bfs(i)
                components += 1
        
        return components


s = Solution()
print(s.countComponents(5, [[0,1],[1,2],[2, 0],[3,4]]))