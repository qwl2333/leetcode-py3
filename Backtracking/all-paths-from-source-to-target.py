# lc 797
from collections import deque
class Solution:
    '''
    how many path from node 0 to node n-1
    first of all, assuming 0 -> n-1 already exist
    for the rest n - 2 nodes, each node could choose to be added to the path or not added to the path
    so 2^(n-2)
    So TC is roughly O(2^n)
    '''
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        visited = list()
        self.res = []
        def dfs(node: int):
            if node == n - 1:
                self.res.append(list(visited))
                return

            for nb in graph[node]:
                visited.append(nb)
                dfs(nb)
                visited.pop()

        visited.append(0)
        dfs(0)
        return self.res

    def allPathsSourceTargetBFS(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        queue = deque()
        queue.append((0, [0]))
        res = []

        while queue:
            cur_idx, cur_path = queue.popleft()
            neighbours = graph[cur_idx]
            for nb in neighbours:
                new_path = cur_path + [nb]
                if nb == n - 1:
                    res.append(new_path)
                else:
                    queue.append((nb, new_path))

        return res

s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))