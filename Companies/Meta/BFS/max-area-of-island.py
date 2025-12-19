# lc 695
from collections import deque
class Solution:
    '''
    TC O(r * c) r - row number, c - col number
    SC O(min(r, c))
    Say every cell is 1,
    Imagine a large grid where every cell is 1. If you start BFS from the top-left corner 
    (0,0) :
    Level 0: Queue contains 1 node: (0,0)
    Level 1: Queue contains 2 nodes: (0,1), (1,0).
    Level 2: Queue contains 3 nodes: (0,2), (1,1), (2,0).
    Level 3: Queue contains 4 nodes: (0,3), (1,2), (2,1), (3,0).
    The BFS expands like a "diagonal wave" or a ripple in a pond.
    The queue only ever stores the current frontier (the edge of the wave).
    In a rectangular grid of size r * c:
    The length of this diagonal "frontier" grows as you move toward the center.
    The longest possible diagonal in a rectangle is limited by its shortest side.
    If the grid is 10 * 100, the "wave" can never be wider than roughly 10 cells. 
    Once the wave hits the top and bottom boundaries, it can't grow any wider; it just slides across the remaining length of the rectangle.
    '''
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        # calculate the area of island from (i, j)
        def bfs_helper(i: int, j: int) -> int: 
            area = 0
            queue = deque()
            queue.append((i, j))
            grid[i][j] = 0

            dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
            while queue:
                cur_x, cur_y = queue.popleft()
                area += 1
                for dx, dy in dirs:
                    new_x = cur_x + dx
                    new_y = cur_y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 0
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                area = bfs_helper(i, j)
                max_area = max(max_area, area)

        return max_area