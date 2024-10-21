# lc 1091
from collections import deque, defaultdict
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0 and n == 1:
            return 1
    
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        queue = deque()
        visited = set()
        if grid[0][0] == 0:
            queue.append((0, 0))
            visited.add((0, 0))

        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        if new_x == n - 1 and new_y == n - 1:
                            return steps + 2
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            steps += 1
        return -1

    # find all paths with shortest path length 和 word ladder 2 解法类似
    def shortestPathBinaryMatrix2(self, grid: list[list[int]]) -> list[list[tuple]]:
        n = len(grid)
        if grid[0][0] == 0 and n == 1:
            return [[(0, 0)]]

        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        graph = defaultdict(list) # (x, y) -> [(a, b), (c, d)..]
        visited = {} # (x, y) -> min distance from (0, 0)
        def bfs_build_graph_with_weights():
            queue = deque()
            
            if grid[0][0] == 0:
                queue.append((0, 0))
                visited[(0, 0)] = 0

            steps = 0
            while queue:
                size = len(queue)
                steps += 1
                for i in range(size):
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy
                        if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                            graph[(x, y)].append((new_x, new_y)) # 不能把这个放到59行里,如果放59行下面,之前visited过的节点到当前节点的边界信息就不会被加进graph里了
                            if (new_x, new_y) not in visited:
                                queue.append((new_x, new_y))
                                visited[(new_x, new_y)] = steps
        
        bfs_build_graph_with_weights()
        result = []
        def dfs(x: int, y: int, end_x: int, end_y, path: list[tuple]):
            if x == end_x and y == end_y:
                result.append(list(path))
                return

            for nbx, nby in graph[(x, y)]:
                if visited[(nbx, nby)] == visited[(x, y)] + 1:
                    path.append((nbx, nby))
                    dfs(nbx, nby, end_x, end_y, path)
                    path.pop()

        path = list()
        path.append((0, 0))
        dfs(0, 0, n - 1, n - 1, path)
        return result                            
        
s = Solution()
print(s.shortestPathBinaryMatrix2([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]))