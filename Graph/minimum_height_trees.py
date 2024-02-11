from collections import deque
class Solution:
    # 类似topological sort的方法，把入度为1的叶子一轮一轮的裁剪，直到剩下<=2个节点时，就是剩下两个以内，
    # 此题是tree，裁剪剩下的tree，一定只会剩下一个或者两个点
    # Time, space O(n + v) - n number of nodes, v number of edges
    def findMinHeightTreesTopo(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1: 
            return [0] 
        graph = {i:set() for i in range(n)}
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
        
        queue = deque([])
        for i in range(n):
            if len(graph[i]) == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size
            for i in range(size):
                cur = queue.popleft()
                for nb in graph[cur]:
                    graph[nb].remove(cur)
                    if len(graph[nb]) == 1:
                        queue.append(nb)
                        
        return list(queue)

    # 最笨的方法 每一个点做bfs看height tle
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = {i:[] for i in range(n)}
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        def bfs(start: int) -> int:
            queue = deque([start])
            height = -1
            visited = set([start])
            while queue:
                size = len(queue)
                for i in range(size):
                    cur = queue.popleft()
                    for nb in graph[cur]:
                        if nb not in visited:
                            visited.add(nb)
                            queue.append(nb)
                height += 1
            return height

        res = []
        min_height = float('inf')
        for i in range(n):
            height = bfs(i)
            if height < min_height:
                min_height = height
                res = []
                res.append(i)
            elif height == min_height:
                res.append(i)

        return res
                