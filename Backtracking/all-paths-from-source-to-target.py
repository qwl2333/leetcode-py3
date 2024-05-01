# lc 797
class Solution:
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

s = Solution()
print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))