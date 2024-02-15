# lc 417
from collections import deque
class Solution:
    # Time O(n * m)
    # 此题是问哪些点可以同时到达atlantic和pacific边界，点移动的条件是海拔高可往低的移动
    # 从 atlantic边界 和 pacific边界 各做一次bfs，同时visited过的就是可以到达两片海域的
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n = len(heights)
        m = len(heights[0])

        visited = set()
        queue = deque()
        for i in range(n):
            queue.append((i, 0))
            visited.add((i, 0))
        for j in range(1, m):
            queue.append((0, j))
            visited.add((0, j))

        def bfs(queue: deque):
            while queue:
                x, y = queue.popleft()
                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in visited:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
        
        bfs(queue)
        c_to_p = list(visited)
        print(c_to_p)
        visited = set()
        for i in range(n):
            queue.append((i, m - 1))
            visited.add((i, m - 1))
        for j in range(0, m - 1):
            queue.append((n - 1, j))
            visited.add((n - 1, j))
        bfs(queue)
        print(visited)
        res = []
        for c in c_to_p:
            if c in visited:
                res.append(list(c))

        return res