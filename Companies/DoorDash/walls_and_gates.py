# lc 286 和 lc 317不同，317是到所有源点距离之和, 286是到最近源点的距离
from collections import deque
class Solution:
    # multi resource BFS time space O(n*m)
    # Time (n*m), space O(n*m)
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        INF = 2147483647

        queue = deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        path = 1
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and rooms[new_x][new_y] == INF:
                        rooms[new_x][new_y] = path
                        queue.append((new_x, new_y))
            path += 1
        
        return rooms

    # DFS + memo TLE O(n*m  * n*m)  n*m个元素，每个dfs最差都是n*m
    def wallsAndGatesDFS(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        INF = 2147483647

        def dfs(r: int, c: int) -> int:
            if rooms[r][c] == 0:
                return 0
            if rooms[r][c] == -1:
                return INF
            if rooms[r][c] != INF:
                return rooms[r][c]
            
            visited.add((r, c))
            min_dist = INF
            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < n and 0 <= new_c < m and (new_r, new_c) not in visited:
                    dist = dfs(new_r, new_c)
                    min_dist = min(min_dist, dist + 1)
            visited.remove((r, c))

            rooms[i][j] = min_dist
            return min_dist
        
        for i in range(n):
            for j in range(m):
                dfs(i, j)
        
        return rooms
            
        