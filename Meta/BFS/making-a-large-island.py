# lc 827
from collections import deque
class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def mark_an_island_bfs(start_row: int, start_col: int, new_value: int) -> int: # bfs
            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = new_value
            counter = 1
            while queue:
                cur_r, cur_c = queue.popleft()
                for dr, dc in directions:
                    new_r = cur_r + dr
                    new_c = cur_c + dc
                    if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = new_value
                        counter += 1
            return counter
        
        new_value = 2
        new_value_to_area = {}
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = mark_an_island_bfs(i, j, new_value)
                    new_value_to_area[new_value] = area
                    res = max(res, area)
                    new_value += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    accum_area = 1
                    different_values = set()
                    for dr, dc in directions:
                        new_r = dr + i
                        new_c = dc + j
                        if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] != 0 and grid[new_r][new_c] not in different_values:
                            accum_area += new_value_to_area[grid[new_r][new_c]]
                            different_values.add(grid[new_r][new_c])
                    res = max(res, accum_area)
        
        return res

    def largestIslandDFS(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def mark_an_island_dfs(row: int, col: int, new_value: int) -> int: # dfs
            if 0 > row or row >= n or 0 > col or col >= n or grid[row][col] != 1:
                return 0

            grid[row][col] = new_value
            area = 1
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                area += mark_an_island_dfs(new_r, new_c, new_value)
 
            return area
        
        new_value = 2
        new_value_to_area = {}
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area = mark_an_island_dfs(i, j, new_value)
                    new_value_to_area[new_value] = area
                    res = max(res, area)
                    new_value += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    accum_area = 1
                    different_values = set()
                    for dr, dc in directions:
                        new_r = dr + i
                        new_c = dc + j
                        if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] != 0 and grid[new_r][new_c] not in different_values:
                            accum_area += new_value_to_area[grid[new_r][new_c]]
                            different_values.add(grid[new_r][new_c])
                    res = max(res, accum_area)
        
        return res